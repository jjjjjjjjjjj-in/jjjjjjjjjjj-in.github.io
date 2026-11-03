// マーベル映画紹介・特集ページ・もっちぃまのトップの共有画像（og.png, 1200x630）を作る。
// 使い方: node src/og_pages.js （リポジトリのルートで実行）
const {chromium} = require('playwright');
const FONT = '<link href="https://fonts.googleapis.com/css2?family=Anton&family=Zen+Kaku+Gothic+New:wght@700;900&display=swap" rel="stylesheet">';
const marvel = (title, sub, kicker) => `<div class="m"><div class="k">${kicker}</div><div class="t">${title}</div><div class="s">${sub}</div><div class="bar"></div></div>`;
const PAGES = [
  ['marvel/og.png', marvel('マーベル映画紹介', '観る順番・あらすじ・相関図を、作品ごとにやさしく解説', 'MOVIE GUIDE')],
  ['marvel/en/og.png', marvel('Marvel Movie Guides', 'Watch order, story, character maps and key terms', 'MOVIE GUIDE')],
  ['marvel/timeline/og.png', marvel('MCU完全年表', '宇宙の誕生から最新作まで、物語の時代順に', 'MCU TIMELINE')],
  ['marvel/box-office/og.png', marvel('興行収入ランキング', 'マーベル作品の世界興行収入と歴代順位', 'BOX OFFICE')],
  ['marvel/rerelease/og.png', marvel('再上映情報', 'マーベル作品の再上映・リバイバル上映のまとめ', 'RE-RELEASE')],
  ['paradise-city/og.png', '<div class="pc"><div class="pck">PARADISE CITY GUIDE</div><div class="pct">パラダイスシティ<br>カジノガイド</div><div class="pcs">日本人向け お得情報・宿泊・行き方</div></div>'],
  ['og.png', '<div class="p"><div class="pt">もっちぃま</div></div>'],
];
const CSS = `html,body{margin:0}
.m,.p,.pc{width:1200px;height:630px;position:relative;overflow:hidden;box-sizing:border-box}
.m{background:radial-gradient(circle at 80% 20%,#3a0d0d,#0b0b0d 60%);color:#fff;padding:90px 90px;font-family:'Zen Kaku Gothic New',IPAGothic,sans-serif}
.k{font-family:Anton,sans-serif;letter-spacing:.14em;color:#e23636;font-size:34px}
.t{font-weight:900;font-size:96px;line-height:1.15;margin-top:30px}
.s{font-weight:700;font-size:36px;color:#d9d9e0;margin-top:30px}
.bar{position:absolute;left:0;right:0;bottom:0;height:28px;background:#e23636}
.pc{background:linear-gradient(90deg,rgba(7,11,26,.9) 40%,rgba(7,11,26,.15)),url(paradise-city/img/pegasus.jpg) right center/cover;padding:90px;color:#fff;font-family:'Zen Kaku Gothic New',IPAGothic,sans-serif}
.pck{font-family:Anton,sans-serif;letter-spacing:.14em;color:#e9c46a;font-size:32px}
.pct{font-weight:900;font-size:84px;line-height:1.2;margin-top:24px}
.pcs{font-weight:700;font-size:34px;color:#e9c46a;margin-top:28px}
.p{background:linear-gradient(160deg,#ff8fc0,#f0559a);display:flex;align-items:center;justify-content:center}
.pt{color:#fff;font-family:'Zen Kaku Gothic New',IPAGothic,sans-serif;font-weight:900;font-size:150px;text-shadow:0 6px 0 rgba(160,20,80,.35)}`;
(async () => {
  const b = await chromium.launch(); const p = await b.newPage({viewport: {width: 1200, height: 630}});
  for (const [out, html] of PAGES) {
    await p.goto('file://' + process.cwd() + '/index.html'); await p.setContent(`<html><head><base href="file://${process.cwd()}/">${FONT}<style>${CSS}</style></head><body>${html}</body></html>`, {waitUntil: 'networkidle'});
    await p.evaluate(() => document.fonts.ready); await p.waitForTimeout(300);
    await p.screenshot({path: out}); console.log('og:', out);
  }
  await b.close();
})();
