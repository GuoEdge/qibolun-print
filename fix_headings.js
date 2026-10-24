const fs = require('fs');

const file = '/storage/Users/currentUser/Documents/岐伯论/research-rebuild/reports/qibo_wenxuan_essential_doctrines.md';
let content = fs.readFileSync(file, 'utf8');

// 二级标题：第X论 → X (繁体)
const chapNumMap = {
  '第二论': '叁',
  '第三论': '肆',
  '第四论': '伍',
  '第五论': '陆',
  '第六论': '柒',
  '第七论': '捌'
};

// 三级标题：一、二、三 → 其一·、其二·、其三·
for (const [old, cn] of Object.entries(chapNumMap)) {
  const regex = new RegExp(`^## ${old}·`, 'gm');
  content = content.replace(regex, `## ${cn}·`);
}

// 替换三级标题
content = content.replace(/^### 一、 /gm, '### 其一· ');
content = content.replace(/^### 二、 /gm, '### 其二· ');
content = content.replace(/^### 三、 /gm, '### 其三· ');
content = content.replace(/^### 四、 /gm, '### 其四· ');

fs.writeFileSync(file, content, 'utf8');
console.log('格式统一完成');
