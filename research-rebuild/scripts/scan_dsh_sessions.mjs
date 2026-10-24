import fs from 'node:fs'
import path from 'node:path'
import zlib from 'node:zlib'
import { Readable } from 'node:stream'
import { finished } from 'node:stream/promises'

const root = process.argv[2] || '/home/gcj/.dsh/sessions'
const terms = (process.argv.slice(3).length ? process.argv.slice(3) : ['素问','sooon','q9adg','岐伯论']).map(x => x.toLowerCase())
function walk(dir) {
  const out = []
  for (const ent of fs.readdirSync(dir, {withFileTypes:true})) {
    const p = path.join(dir, ent.name)
    if (ent.isDirectory()) out.push(...walk(p))
    else if (ent.isFile() && ent.name.endsWith('.zstd')) out.push(p)
  }
  return out
}
for (const file of walk(root)) {
  let text
  try {
    const chunks = []
    const input = Readable.from([fs.readFileSync(file)])
    const dec = input.pipe(zlib.createZstdDecompress())
    dec.on('data', c => chunks.push(c))
    await finished(dec)
    text = Buffer.concat(chunks).toString('utf8')
  }
  catch { continue }
  const low = text.toLowerCase()
  const hits = terms.filter(t => low.includes(t))
  if (!hits.length) continue
  console.log(JSON.stringify({file, hits, bytes:text.length}))
  const lines = text.split(/\r?\n/).filter(line => terms.some(t => line.toLowerCase().includes(t)))
  for (const line of lines.slice(0, 8)) console.log(line.slice(0, 1200))
}
