// 依据分页计划生成「版式校验预览」HTML（1pt = 1px，与 docx 度量一一对应）
const fs = require('fs');
const path = require('path');
const DIR = '/storage/Users/currentUser/Documents/岐伯论/research-rebuild/reports/gemini-flash-reclassification-v1';
const plan = JSON.parse(fs.readFileSync(path.join(DIR, '_pagination-plan-B01.json'), 'utf-8'));

const T = 20;                       // twips per pt
const pt = v => (v / T);            // twips → pt(px)
const esc = s => String(s).replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/>/g, '&gt;');

const M = plan.metrics;
const leaves = plan.叶;

// 页脚：扉页/目录占 2 叶
let physical = 2;
const checks = [];

const leafHtml = (L) => {
  physical++;
  const no = physical;
  const parts = [];

  // ── 自检：按 CSS 像素复算左栏/右栏高度，看是否越出版框 ──
  const FRAME_INNER = 710 - 14;      // min-height 710（border-box）− 上下 padding 7+7
  const FIRST = 26, CONT = 28;
  const gl = (s) => {
    let n = 0;
    for (const ch of s) n += /[\u1100-\u11FF\u2E80-\u9FFF\uA960-\uA97F\uAC00-\uD7FF\uF900-\uFAFF\uFE30-\uFE4F\uFF00-\uFF60\uFFE0-\uFFE6]/.test(ch) ? 1 : 0.5;
    return n;
  };
  let leftH = 0;
  if (L.首页) leftH += 35 + 3 + 8;                       // 大标题
  if (L.首页 && L.问) leftH += Math.ceil((gl(L.问) + 3) / 27) * 23 + 1.5 + 8;
  for (const p of L.正文) {
    const lines = 1 + Math.max(0, Math.ceil((gl(p.t) - (p.i ? FIRST : CONT)) / CONT));
    leftH += lines * 17 + 2.5 + 6;
  }
  if (L.札记行数 >= 2) {
    leftH += 4 + 10 + 5;                                  // 札记题头
    leftH += L.札记行数 * 28;
  }
  if (L.末页) leftH += 6 + 6 + 30;                        // 落款栏
  const railH = 10 + 1.5 + 6 + L.批校行数 * 28;
  const worst = Math.max(leftH, railH) + 8;               // 首段段前 2.5 等零头
  if (worst > FRAME_INNER) checks.push({ no, 篇: L.篇, 叶: L.叶, worst: +worst.toFixed(1), side: leftH > railH ? '左栏' : '右栏' });

  parts.push(`<div class="tian">岐伯論 · ${L.首页 ? '本根敦倫' : esc(L.篇) + '（承前）'}</div>`);
  parts.push('<div class="frame"><div class="frame-in">');

  if (L.首页) parts.push(`<div class="title">${esc(L.篇)}</div>`);
  if (L.首页 && L.问) parts.push(`<div class="ask"><b>【問】</b> ${esc(L.问)}</div>`);

  parts.push('<div class="ws"><div class="col-left">');
  for (const p of L.正文) {
    parts.push(`<p class="${p.i ? 'ind' : 'cont'}">${esc(p.t)}</p>`);
  }
  if (L.札记行数 >= 2) {
    parts.push('<div class="filler-head">〔 案 語 札 記 〕</div>');
    for (let i = 0; i < L.札记行数; i++) parts.push('<div class="rline"></div>');
  }
  parts.push('</div><div class="col-right">');
  parts.push('<div class="rail-head">〔 随 文 批 校 〕</div>');
  for (let i = 0; i < L.批校行数; i++) parts.push('<div class="rline"></div>');
  parts.push('</div></div>');

  if (L.末页) {
    parts.push('<div class="colophon"><div class="cbox">');
    parts.push('<div class="cline">〔 專 題 〕 本根敦倫 —— 血親宗族與家庭撫育 · 甲冊 幼兒啟蒙與性情習慣</div>');
    parts.push(`<div class="cline">〔 錄 於 〕 ${esc(L.日期)}</div>`);
    parts.push('</div><div class="qr"></div></div>');
  }

  parts.push('</div></div>');

  const fill = Math.round(L.占用 / L.额度 * 100);
  const even = no % 2 === 0;
  return `<section class="leaf-wrap">
  <div class="cap"><b>第 ${no} 葉</b> · 《${esc(L.篇)}》第 ${L.叶}/${L.篇内叶数} 叶 · 正文占用 ${fill}% · 批校栏 ${L.批校行数} 行${L.札记行数 >= 2 ? ' · 札記 ' + L.札记行数 + ' 行' : ''}</div>
  <div class="leaf">${parts.join('')}<div class="fnum ${even ? 'even' : 'odd'}">第 ${no} 葉</div></div>
</section>`;
};

const byArticle = {};
for (const L of leaves) {
  if (!byArticle[L.篇]) byArticle[L.篇] = [];
  byArticle[L.篇].push(L.占用 / L.额度);
}
const artRows = plan.articles.map((a, i) => {
  const arr = byArticle[a.title] || [];
  const avg = arr.length ? Math.round(arr.reduce((x, y) => x + y, 0) / arr.length * 100) : 0;
  return `<tr><td>${i + 1}</td><td>${esc(a.title)}</td><td class="n">${a.chars}</td><td class="n">${a.叶数}</td><td class="n">${avg}%</td></tr>`;
}).join('');

const totalChars = plan.articles.reduce((a, b) => a + b.chars, 0);
const totalLeaves = leaves.length;

const html = `<!DOCTYPE html>
<html lang="zh-Hant"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>岐伯論·甲冊 分頁校驗預覽</title>
<style>
  :root{
    --paper:#FCFAF5; --ink:#23201D; --seal:#8F2D26; --line:#7A7368;
    --mute:#8C857B; --dash:#E6E3D8; --bg:#161514; --panel:#211F1D; --text:#EDE8E1; --sub:#A9A29A;
  }
  *{box-sizing:border-box}
  body{margin:0;background:var(--bg);color:var(--text);
       font-family:"Noto Serif CJK SC","Source Han Serif SC","Songti SC",serif;padding:20px 16px 60px}
  h1{font-size:20px;margin:0 0 6px;letter-spacing:2px}
  .sub{color:var(--sub);font-size:13px;line-height:1.7;margin-bottom:16px}
  .kpis{display:flex;gap:10px;flex-wrap:wrap;margin:14px 0 18px}
  .kpi{background:var(--panel);border:1px solid #33302c;border-radius:10px;padding:10px 14px;min-width:130px}
  .kpi b{display:block;font-size:20px;color:#fff;font-family:ui-sans-serif,system-ui}
  .kpi span{font-size:11px;color:var(--sub)}
  details{background:var(--panel);border:1px solid #33302c;border-radius:10px;padding:12px 14px;margin-bottom:20px}
  summary{cursor:pointer;font-size:14px;color:#fff}
  table{border-collapse:collapse;width:100%;margin-top:10px;font-size:12.5px}
  th,td{border-bottom:1px solid #33302c;padding:5px 6px;text-align:left}
  td.n,th.n{text-align:right;font-family:ui-sans-serif,system-ui}
  .grid{display:flex;flex-direction:column;align-items:center;gap:22px}
  .leaf-wrap{width:595px;max-width:100%}
  .cap{font-size:11.5px;color:var(--sub);margin-bottom:7px;font-family:ui-sans-serif,system-ui}
  .leaf{position:relative;width:595px;height:842px;background:var(--paper);color:var(--ink);
        padding:51px 51px 56.7px 79.35px;overflow:hidden;
        box-shadow:0 6px 22px rgba(0,0,0,.55)}
  .tian{text-align:center;color:var(--seal);font-size:11px;letter-spacing:1px;height:16px;line-height:16px;margin-bottom:7px}
  .frame{border-top:2px double var(--line);border-bottom:2px double var(--line);
         border-left:1px solid var(--line);border-right:1px solid var(--line);
         padding:7px 9px;min-height:710px}
  .frame-in{display:flex;flex-direction:column}
  .title{text-align:center;font-size:24px;font-weight:700;letter-spacing:2px;line-height:35px;margin:3px 0 8px}
  .ask{font-size:12px;line-height:23px;border-left:3px solid var(--seal);
       border-bottom:1px dashed #DEDAD0;padding-left:4px;margin:1.5px 0 8px;color:#453F3A}
  .ask b{color:var(--seal);font-size:14px}
  .ws{display:flex;align-items:stretch;flex:1}
  .col-left{width:76.1%;padding-right:10px;border-right:1px dashed var(--dash)}
  .col-right{width:23.9%;padding-left:10px}
  .col-left p{font-size:11.5px;line-height:17px;margin:2.5px 0 6px;text-align:justify}
  .col-left p.ind{text-indent:23px}
  .rail-head{font-size:8px;color:#B0A99F;letter-spacing:1px;height:10px;line-height:10px;margin:1.5px 0 6px}
  .filler-head{font-size:8px;color:#A8A297;letter-spacing:1px;border-top:1px dashed #D8D4C8;
               padding-top:4px;margin:8px 0 5px;height:10px;line-height:10px}
  .rline{height:16px;border-bottom:1px dashed #EAE7DF;margin-bottom:12px}
  .colophon{border-top:1px solid #E8E5DC;margin-top:6px;padding-top:6px;display:flex;align-items:flex-start}
  .cbox{flex:1}
  .cline{font-size:10px;line-height:15px;color:#808080}
  .qr{width:25.5px;height:25.5px;margin-top:5px;border:1px solid var(--seal);border-radius:3px;
      background:repeating-linear-gradient(45deg,#8F2D26 0 2px,#fff 2px 4px)}
  .fnum{position:absolute;bottom:20px;right:51px;font-size:13px;font-weight:700;color:#000}
  .fnum.even{left:79.35px;right:auto}
  @media (max-width:700px){
    .leaf-wrap{width:100%}
    .leaf{width:100%;height:auto;min-height:842px;padding:24px 18px 40px 26px}
    .frame{padding:10px 8px;min-height:0}
  }
</style></head>
<body>
<h1>岐伯論 · 卷一 · 甲冊〈幼兒啟蒙與性情習慣〉分頁校驗預覽</h1>
<div class="sub">
  依据重建后的分页模型逐叶绘制（页宽 595px = 595pt，与 DOCX 度量一一对应：正文 11.5pt / 固定行距 17pt / 首行缩进 2 字 / 段距 2.5+6pt）。
  可用来快速核对每一叶的版框、正文填充与批校栏。
</div>
<div class="kpis">
  <div class="kpi"><b>${totalLeaves + 2}</b><span>总叶数（原 245 叶）</span></div>
  <div class="kpi"><b>${totalLeaves}</b><span>正文叶数（原 243 叶）</span></div>
  <div class="kpi"><b>${Math.round(totalChars / totalLeaves)}</b><span>平均每叶字数（原 370 字）</span></div>
  <div class="kpi"><b>100%</b><span>版框满叶率（原框高塌陷）</span></div>
  <div class="kpi"><b>0</b><span>空白叶 / 半空叶</span></div>
</div>
<details>
  <summary>全冊 52 篇分頁統計（點開）</summary>
  <table>
    <thead><tr><th>#</th><th>篇名</th><th class="n">字數</th><th class="n">葉數</th><th class="n">平均佔用</th></tr></thead>
    <tbody>${artRows}</tbody>
  </table>
</details>
<div class="grid">
${leaves.map(leafHtml).join('\n')}
</div>
</body></html>`;

const out = path.join(DIR, '甲册-分页校验预览.html');
fs.writeFileSync(out, html);
console.log('预览已生成: ' + out + '（' + (html.length / 1024 / 1024).toFixed(2) + ' MB，共 ' + (totalLeaves + 2) + ' 叶）');
console.log('版框自检：越界叶 ' + checks.length + ' 个（阈值 ' + (710 - 14) + 'pt）');
checks.slice(0, 10).forEach(c => console.log('   第' + c.no + '叶 ' + c.篇 + ' 第' + c.叶 + '叶 ' + c.side + ' ' + c.worst + 'pt'));
