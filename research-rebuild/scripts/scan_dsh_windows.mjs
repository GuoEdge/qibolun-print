import fs from 'node:fs'
import path from 'node:path'
import zlib from 'node:zlib'
const root = process.argv[2] || '\\\\wsl$\\Ubuntu-24.04\\home\\gcj\\.dsh\\sessions'
const terms = ['素问','sooon','q9adg','publishedAt','4296','全量阅读']
let n=0
async function walk(d){
  for(const e of fs.readdirSync(d,{withFileTypes:true})){
    const p=path.join(d,e.name)
    if(e.isDirectory()) await walk(p)
    else if(e.isFile() && e.name.endsWith('.zstd')){
      try{
        const b=fs.readFileSync(p), starts=[]
        for(let i=0;i+4<=b.length;i++) if(b[i]===0x28&&b[i+1]===0xb5&&b[i+2]===0x2f&&b[i+3]===0xfd) starts.push(i)
        const chunks=[]
        for(let i=0;i<starts.length;i++) chunks.push(zlib.zstdDecompressSync(b.subarray(starts[i], starts[i+1] ?? b.length)))
        const s=Buffer.concat(chunks).toString()
        if(s.length>500 && terms.some(t=>s.includes(t))){
          console.log(JSON.stringify({file:p,len:s.length,hits:terms.filter(t=>s.includes(t))}))
          for(const l of s.split(/\r?\n/).filter(x=>terms.some(t=>x.includes(t))).slice(0,4)) console.log(l.slice(0,1000))
          n++
        }
      }catch{}
    }
  }
}
await walk(root); console.error('MATCHES',n)
