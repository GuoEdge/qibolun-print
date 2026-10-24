from pathlib import Path
from PIL import Image, ImageDraw
src=Path(__file__).resolve().parents[1]/'image-review'/'round116b'
files=sorted(src.glob('*.jpg'))
for start in range(0,len(files),10):
    group=files[start:start+10]; cols=2; tw,th,lh=620,430,34
    sheet=Image.new('RGB',(cols*tw,((len(group)+1)//2)*(th+lh)),'white'); d=ImageDraw.Draw(sheet)
    for j,p in enumerate(group):
        with Image.open(p) as im:
            im=im.convert('RGB'); im.thumbnail((tw-12,th-12))
            x=j%cols*tw+(tw-im.width)//2; y=j//cols*(th+lh)+(th-im.height)//2
            sheet.paste(im,(x,y))
        d.text((j%cols*tw+6,j//cols*(th+lh)+th+6),p.name,fill='black')
    out=src/f'sheet-{start+1:02d}-{start+len(group):02d}.jpg'; sheet.save(out,quality=90); print(out)
