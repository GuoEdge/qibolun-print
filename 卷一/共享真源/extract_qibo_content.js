// 岐伯論 · 语料内容抽取器（提问者叙述 vs 岐伯回答 分离）
// ---------------------------------------------------------------------------
// 背景：sooon.ai 的 answer 是 Lexical 结构化 JSON。其中：
//   type=quote      → 提问者长叙述 / 引用的原文材料（第一人称讲故事）
//   type=paragraph  → 岐伯本人的回答正文
//   type=heading    → 少数文章的小标题（归入回答）
// 文本叶子节点有两种历史格式：type=text 与 type=p-text，二者都带 text 字段。
// 本地 `text` 字段是把 quote+paragraph 拍扁合并的结果，丢失了边界，导致排版时
// 把「提问者叙述」误排进「岐伯答」正文。本模块从 lexical 精确恢复边界。
//
// 用法：
//   const X = require('./extract_qibo_content.js');
//   const { narrative, answer, usedLexical } = X.extract(record.lexical);
//   // narrative = 提问者长叙述（可能为空字符串）
//   // answer    = 岐伯回答正文（段落以 \n 分隔）
// ---------------------------------------------------------------------------

function blockText(blockNode) {
  const parts = [];
  function rec(n) {
    if (Array.isArray(n)) { for (const v of n) rec(v); return; }
    if (!n || typeof n !== 'object') return;
    if (typeof n.text === 'string' && n.text) parts.push(n.text);
    else if (n.type === 'linebreak') parts.push('\n');
    for (const k of Object.keys(n)) {
      const v = n[k];
      if (v && typeof v === 'object') rec(v);
    }
  }
  rec(blockNode);
  return parts.join('');
}

// 顶层块路由：quote → 叙述；其余（paragraph/heading/link/list/horizontalrule/image…）→ 回答
const ANSWER_BLOCK_TYPES = new Set(['paragraph', 'heading', 'link', 'list', 'image']);

function walkBlocks(node, narrative, answer) {
  if (Array.isArray(node)) { for (const v of node) walkBlocks(v, narrative, answer); return; }
  if (!node || typeof node !== 'object') return;
  const t = node.type;
  if (t === 'quote') { const txt = blockText(node).trim(); if (txt) narrative.push(txt); return; }
  if (ANSWER_BLOCK_TYPES.has(t)) { const txt = blockText(node).trim(); if (txt) answer.push(txt); return; }
  for (const k of Object.keys(node)) {
    const v = node[k];
    if (v && typeof v === 'object') walkBlocks(v, narrative, answer);
  }
}

function normalize(s) {
  return s
    .replace(/\r\n/g, '\n')
    .replace(/\n{2,}/g, '\n')
    .split('\n').map(x => x.trim()).filter(Boolean).join('\n');
}

// 解析单条 lexical，返回 { narrative, answer, usedLexical }
function extract(lexical) {
  if (typeof lexical !== 'string' || !lexical.trim().startsWith('{')) {
    return { narrative: '', answer: '', usedLexical: false };
  }
  try {
    const root = JSON.parse(lexical);
    const narrative = [];
    const answer = [];
    walkBlocks(root, narrative, answer);
    return {
      narrative: normalize(narrative.join('\n')),
      answer: normalize(answer.join('\n')),
      usedLexical: true
    };
  } catch (e) {
    return { narrative: '', answer: '', usedLexical: false, error: String(e) };
  }
}

// 从一条语料记录里取「干净正文 + 提问者叙述」。
// 返回 { answer, narrative }：优先用 lexical 解析结果，解析失败则回退 text。
function resolveContent(record) {
  const r = extract(record && record.lexical);
  if (r.usedLexical && r.answer) {
    return { answer: r.answer, narrative: r.narrative, source: 'lexical' };
  }
  return { answer: normalize((record && record.text) || ''), narrative: r.narrative || '', source: 'text' };
}

module.exports = { extract, resolveContent, blockText };

if (require.main === module) {
  const fs = require('fs');
  const lines = fs.readFileSync(process.argv[2] || 'all-articles-merged-v3.jsonl', 'utf-8').trim().split('\n');
  const data = {};
  for (const l of lines) { const d = JSON.parse(l); data[d.title] = d; }
  const titles = process.argv.slice(3);
  if (!titles.length) titles.push('一碗油盐饭', '奠仪几何', 'NPC', '政策观察', '反犹');
  for (const t of titles) {
    const d = data[t];
    if (!d) { console.log('未找到《' + t + '》'); continue; }
    const r = extract(d.lexical);
    console.log('=== 《' + t + '》===');
    console.log('  question:', JSON.stringify((d.question || '').slice(0, 40)));
    console.log('  narrative(' + r.narrative.length + '):', JSON.stringify(r.narrative.slice(0, 50)));
    console.log('  answer(' + r.answer.length + '):', JSON.stringify(r.answer.slice(0, 50)));
    if (r.error) console.log('  ERROR:', r.error);
  }
}
