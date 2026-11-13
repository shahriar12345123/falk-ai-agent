import zlib,struct,math,os
W=H=256
def px(x,y):
    bg=(255,228,236)
    cx,cy=128,140
    # ears
    for ex in (78,178):
        if (x-ex)**2+(y-62)**2<26**2: return (255,200,120) if (x-ex)**2+(y-66)**2>12**2 else (255,170,170)
    if ((x-cx)/92)**2+((y-cy)/80)**2<1:
        for ex in (96,160):
            if (x-ex)**2+(y-135)**2<16**2:
                return (255,255,255) if (x-ex-4)**2+(y-131)**2<5**2 else (30,20,30)
        if (x-128)**2+(y-158)**2<6**2: return (240,120,140)
        for ex in (70,186):
            if (x-ex)**2+(y-165)**2<14**2: return (255,150,160)
        return (255,200,120)
    return bg
raw=b''.join(b'\x00'+bytes(c for x in range(W) for c in px(x,y)) for y in range(H))
def ch(t,d):
    c=struct.pack('>I',len(d))+t+d
    return c+struct.pack('>I',zlib.crc32(t+d)&0xffffffff)
png=b'\x89PNG\r\n\x1a\n'+ch(b'IHDR',struct.pack('>IIBBBBB',W,H,8,2,0,0,0))+ch(b'IDAT',zlib.compress(raw,9))+ch(b'IEND',b'')
d=os.environ.get('MAKEFUN_OUTPUT_DIR','/output')
os.makedirs(d,exist_ok=True)
open(os.path.join(d,'entry.png'),'wb').write(png)
