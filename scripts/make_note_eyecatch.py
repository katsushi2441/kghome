#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""note の見出し画像 1280×670。**1200×630 を渡すとスクリプトが待ち続けて落ちる**ので寸法は固定。
ライトテーマ（白＋ティール＋濃紺）＋マスコット。成長する数字は焼き込まない。"""
import os
from PIL import Image, ImageDraw, ImageFont

W, H = 1280, 670
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(ROOT, 'outputs', 'kghome_note84_1280x670.png')
MASCOT = '/home/kojima/work/kurage_web/images/kurage-mascot-cutout.png'
FB = '/usr/share/fonts/opentype/noto/NotoSansCJK-Black.ttc'
FM = '/usr/share/fonts/opentype/noto/NotoSansCJK-Bold.ttc'
FR = '/usr/share/fonts/opentype/noto/NotoSansCJK-Regular.ttc'

os.makedirs(os.path.dirname(OUT), exist_ok=True)
img = Image.new('RGB', (W, H), '#ffffff')
dr = ImageDraw.Draw(img, 'RGBA')
dr.ellipse([-230, -280, 470, 380], fill=(230, 244, 242, 255))
dr.ellipse([W - 450, H - 320, W + 250, H + 270], fill=(239, 246, 246, 255))

mascot = Image.open(MASCOT).convert('RGBA')
mh = 290
mascot = mascot.resize((int(mascot.width * mh / mascot.height), mh))
cx = 520

f_badge = ImageFont.truetype(FM, 26)
f_s = ImageFont.truetype(FR, 25)
f_band = ImageFont.truetype(FM, 28)

badge = '国のオープンデータを数え直した'
bw = dr.textlength(badge, font=f_badge) + 46
dr.rounded_rectangle([cx - bw / 2, 85, cx + bw / 2, 137], radius=26, fill='#e6f4f2', outline='#bfe3de')
dr.text((cx, 111), badge, font=f_badge, fill='#0a726b', anchor='mm')

dr.text((cx, 205), '障害者グループホームは', font=ImageFont.truetype(FB, 45), fill='#12202f', anchor='mm')
dr.text((cx, 283), '1.60倍に増えた。', font=ImageFont.truetype(FB, 50), fill='#0a9a8f', anchor='mm')
dr.text((cx, 355), '同じ期間に入所施設は1.03倍のまま。', font=f_s, fill='#5d6b7a', anchor='mm')
dr.text((cx, 397), '消えた1,618か所は、法人に偏っていました。', font=f_s, fill='#5d6b7a', anchor='mm')

bt = '住まい 28,471事業所を住所ひとつで'
bw2 = dr.textlength(bt, font=f_band) / 2 + 36
dr.rounded_rectangle([cx - bw2, 462, cx + bw2, 522], radius=16, fill='#0a9a8f')
dr.text((cx, 492), bt, font=f_band, fill='#ffffff', anchor='mm')

img.paste(mascot, (W - mascot.width - 42, H - mascot.height - 30), mascot)
dr.text((42, H - 40), 'kurage.exbridge.jp/kghome.php/', font=ImageFont.truetype(FR, 22), fill='#5d6b7a', anchor='lm')
img.save(OUT, optimize=True)
print(OUT, img.size)
