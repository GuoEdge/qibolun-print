// 从all_articles_signals.jsonl提取120篇文章的question字段
const fs = require('fs');
const path = require('path');

const ROOT = path.resolve(__dirname, '../../..');
const ALL_SIGNALS = path.join(ROOT, 'research-rebuild/data/all_articles_signals.jsonl');
const CORPUS_120 = path.join(ROOT, 'research-rebuild/data/qibo_wenxuan_120_final.jsonl');
const OUTPUT = path.join(__dirname, 'questions_map.json');

// 读取120篇文章ID
const selected120 = fs.readFileSync(CORPUS_120, 'utf8')
  .split('\n')
  .filter(Boolean)
  .map(JSON.parse)
  .map(a => a.id);

console.log(`已加载120篇文章ID`);

// 读取全部文章signals，提取question字段
const allSignals = fs.readFileSync(ALL_SIGNALS, 'utf8')
  .split('\n')
  .filter(Boolean)
  .map(JSON.parse);

console.log(`已加载全部文章signals：${allSignals.length} 篇`);

// 构建ID -> question映射
const questionsMap = {};
const selected120Set = new Set(selected120);

for (const article of allSignals) {
  if (selected120Set.has(article.id) && article.question) {
    questionsMap[article.id] = article.question;
  }
}

console.log(`提取到question：${Object.keys(questionsMap).length} / 120 篇`);

// 写入文件
fs.writeFileSync(OUTPUT, JSON.stringify(questionsMap, null, 2), 'utf8');
console.log(`已写入：${OUTPUT}`);
