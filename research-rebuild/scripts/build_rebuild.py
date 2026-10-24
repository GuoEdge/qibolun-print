import argparse,csv,hashlib,json,re
from collections import Counter
from datetime import datetime,timezone,timedelta
from pathlib import Path
TZ=timezone(timedelta(hours=8))
def dt(v):
    try:return datetime.fromtimestamp(int(v)/1000,timezone.utc).astimezone(TZ)
    except:return None
def walk(n,o):
    if isinstance(n,dict):
        if n.get('type'):o.append(n)
        for c in n.get('children') or []:walk(c,o)
def lex(raw):
    x={'types':Counter(),'images':[],'paragraphs':0}
    try:r=json.loads(raw or '{}').get('root',{})
    except:return x
    ns=[];walk(r,ns)
    for n in ns:
        x['types'][str(n.get('type'))]+=1
        if n.get('type')=='image':x['images'].append(n)
        if n.get('type')=='paragraph':x['paragraphs']+=1
    return x
def row(o,i):
    d=dt(o.get('publishedAt'));t=o.get('text') or '';x=lex(o.get('lexical'));u=o.get('url') or ''
    return {'ordinal':i,'source_line':i,'id':o.get('id'),'title':o.get('title') or '','url':u,'published_at':d.isoformat() if d else '','published_date':d.strftime('%Y-%m-%d') if d else '','platform':'zhihu' if 'zhihu' in u else 'afdian' if 'fdian' in u else 'other','text_chars':len(t),'paragraph_count':len([p for p in re.split(r'\r?\n',t) if p.strip()]),'lexical_paragraph_count':x['paragraphs'],'image_count':len(x['images']),'node_types':';'.join(f'{k}:{v}' for k,v in sorted(x['types'].items())),'has_text':bool(t.strip()),'has_provenance':bool(o.get('provenance')),'has_superseded':bool(o.get('superseded'))}
def outcsv(p,rs,fs):
    p.parent.mkdir(parents=True,exist_ok=True)
    with p.open('w',encoding='utf-8-sig',newline='') as f:
        w=csv.DictWriter(f,fieldnames=fs,extrasaction='ignore');w.writeheader();w.writerows(rs)
def choose(rs):
    z=[];seen=set()
    def add(pred,n):
        xs=sorted([r for r in rs if pred(r) and r['id'] not in seen],key=lambda r:(r['published_at'],r['id']))[:n];z.extend(xs);seen.update(r['id'] for r in xs)
    add(lambda r:r['text_chars']==0 and r['image_count']>0,2);add(lambda r:r['image_count']>0 and r['text_chars']>0,4);add(lambda r:r['text_chars']>=10000,3)
    for y in sorted({r['published_date'][:4] for r in rs if r['published_date']}):add(lambda r,y=y:r['published_date'].startswith(y),1)
    add(lambda r:r['platform']=='afdian',3);add(lambda r:r['platform']=='zhihu',3);add(lambda r:r['has_provenance'] or r['has_superseded'],2);add(lambda r:r['has_text'],100)
    return sorted(z[:24],key=lambda r:(r['published_at'],r['id']))
def main():
    ap=argparse.ArgumentParser();ap.add_argument('--corpus',required=True);ap.add_argument('--out',required=True);a=ap.parse_args();c=Path(a.corpus).resolve();o=Path(a.out).resolve();d=o/'data';p=o/'packets'/'calibration';q=o/'records';h=o/'reports'
    for x in(d,p,q,h):x.mkdir(parents=True,exist_ok=True)
    rs=[];raw={};ims=[];errors=[]
    with c.open(encoding='utf-8') as f:
        for i,line in enumerate(f,1):
            try:
                x=json.loads(line);raw[str(x.get('id'))]=x;r=row(x,i);rs.append(r);li=lex(x.get('lexical'))
                for j,im in enumerate(li['images'],1):ims.append({'ordinal':i,'id':x.get('id'),'title':x.get('title') or '','image_index':j,'src':im.get('src',''),'width':im.get('width',''),'height':im.get('height',''),'status':'unreviewed','ocr_status':'not_started','notes':''})
            except Exception as e:errors.append({'line':i,'error':repr(e)})
    rs.sort(key=lambda r:(r['published_at'],r['id']))
    for i,r in enumerate(rs,1):r['reading_ordinal']=i
    fs=list(rs[0]) if rs else [];outcsv(d/'article-index.csv',rs,fs);outcsv(d/'image-inventory.csv',ims,['ordinal','id','title','image_index','src','width','height','status','ocr_status','notes'])
    cal=choose(rs)
    for i,r in enumerate(cal,1):r['calibration_no']=i;r['selection_reason']='stratified calibration sample'
    outcsv(d/'calibration-selection.csv',cal,fs+['calibration_no','selection_reason'])
    now=datetime.now(TZ).isoformat()
    with(q/'reading-records.jsonl').open('w',encoding='utf-8') as f:
        for r in rs:f.write(json.dumps({'reading_ordinal':r['reading_ordinal'],'source_ordinal':r['ordinal'],'id':r['id'],'title':r['title'],'published_date':r['published_date'],'platform':r['platform'],'source_version':'v2-current','text_coverage_status':'unread','understanding_status':'unstarted','image_status':'no_images' if r['image_count']==0 else 'unreviewed','review_status':'not_started','question_context':'','content_units':[],'main_claims':[],'reasoning':[],'concept_usage':[],'examples_and_targets':[],'conditions':[],'rhetoric_and_tone':'','evidence_locations':[],'open_questions':[],'researcher_notes':'','updated_at':now},ensure_ascii=False)+'\n')
    with(q/'review-records.jsonl').open('w',encoding='utf-8') as f:
        for r in rs:f.write(json.dumps({'reading_ordinal':r['reading_ordinal'],'source_ordinal':r['ordinal'],'id':r['id'],'reviewer':'independent','independent_judgment':'','omissions':[],'attribution_issues':[],'modality_issues':[],'terminology_issues':[],'disagreements':[],'resolution':'','review_status':'not_started','updated_at':now},ensure_ascii=False)+'\n')
    for i,r in enumerate(cal,1):
        x=raw[r['id']];t=x.get('text') or '';ps=[z.strip() for z in re.split(r'\r?\n',t) if z.strip()];li=lex(x.get('lexical'));fn=p/f'{i:02d}_{r["reading_ordinal"]:04d}_{r["id"][:8]}.md'
        with fn.open('w',encoding='utf-8') as f:
            f.write(f'# 校准阅读包 {i:02d}｜{x.get("title","")}\n\n- reading_ordinal: {r["reading_ordinal"]}\n- source_ordinal: {r["ordinal"]}\n- id: {r["id"]}\n- date: {r["published_date"]}\n- platform: {r["platform"]}\n- url: {x.get("url","")}\n- image_count: {len(li["images"])}\n\n## 提问字段\n\n{x.get("question") or "[空]"}\n\n## 正文段落\n\n')
            if ps:
                for j,z in enumerate(ps,1):f.write(f'[P{j:03d}] {z}\n\n')
            else:f.write('[TEXT-EMPTY] 需对照图片原件。\n\n')
            f.write('## Lexical结构摘要\n\n'+', '.join(f'{k}={v}' for k,v in sorted(li['types'].items()))+'\n\n')
            for j,im in enumerate(li['images'],1):f.write(f'- image-{j}: {im.get("src","")} ({im.get("width","")}x{im.get("height","")})\n')
            f.write('\n## 精读记录（待填写）\n\n')
            for label in ['具体问题与语境','内容单元','主要主张','论证推进','概念用法','例证与反驳对象','适用条件','修辞与语气','证据定位','未决问题']:f.write(f'### {label}\n\n<!-- 记录原文依据；无此内容时写“本文未说明”。 -->\n\n')
    man={'schema_version':'0.1.0','generated_at':now,'corpus_path':str(c),'corpus_sha256':hashlib.sha256(c.read_bytes()).hexdigest().upper(),'record_count':len(rs),'total_text_chars':sum(r['text_chars'] for r in rs),'date_min':min((r['published_date'] for r in rs if r['published_date']),default=''),'date_max':max((r['published_date'] for r in rs if r['published_date']),default=''),'parse_errors':errors,'duplicate_ids':[k for k,v in Counter(r['id'] for r in rs).items() if v>1],'empty_text_articles':[{'ordinal':r['ordinal'],'id':r['id'],'title':r['title']} for r in rs if not r['has_text']],'image_node_count':len(ims),'image_article_count':len({x['id'] for x in ims}),'calibration_count':len(cal),'status':'PASS' if not errors and len(rs)==4296 else 'REVIEW'}
    (d/'corpus-manifest.json').write_text(json.dumps(man,ensure_ascii=False,indent=2),encoding='utf-8')
    prog={'generated_at':now,'corpus_records':len(rs),'text_coverage_complete':0,'understanding_complete':0,'independent_review_complete':0,'image_review_complete':0,'formal_classification_started':False,'calibration_selected':len(cal),'calibration_reading_complete':0,'calibration_review_complete':0,'notes':'自动盘点完成；没有将任何文章标记为理解完成或复核完成。'}
    (h/'progress.json').write_text(json.dumps(prog,ensure_ascii=False,indent=2),encoding='utf-8')
    (h/'stage-000-inventory.md').write_text(f'# 阶段000｜语料固定与研究底稿初始化\n\n- 语料记录：{len(rs)}\n- SHA-256：{man["corpus_sha256"]}\n- 正文字符：{man["total_text_chars"]:,}\n- 日期范围：{man["date_min"]} 至 {man["date_max"]}\n- 图片文章：{man["image_article_count"]}；图片节点：{man["image_node_count"]}\n- 空正文文章：{len(man["empty_text_articles"])}\n- 校准样本：{len(cal)}\n',encoding='utf-8')
    print(json.dumps(man,ensure_ascii=False,indent=2))
if __name__=='__main__':main()
