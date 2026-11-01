// 作品ガイドの共有画像（/<slug>/og.png と /<slug>/en/og.png）を作る。build.py の後に実行: node src/mcu/render.js
// Playwright と IPAGothic フォントを使う
const { chromium } = require("playwright");
const fs = require("fs");
const path = require("path");

const SRC = __dirname;
const ROOT = path.dirname(path.dirname(SRC));

const esc = (x) => String(x).replace(/[&<>"]/g, (c) => ({ "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;" }[c]));
function filmOg(o) {
  const t = Object.assign({ main: "#1d3a6b", deep: "#0b1a33", accent: "#e5b21a", soft: "#dbe6f5" }, o.theme);
  const ja = o.lang === "ja";
  const big = ja ? o.title : o.title.toUpperCase();
  const size = Math.min(132, Math.floor(900 / (big.length * (ja ? 1 : 0.62))));
  return `<!doctype html><html><head><meta charset="utf-8"><style>
body { margin: 0; width: 1200px; height: 630px; overflow: hidden; color: #fff; font-family: "IPAGothic", sans-serif;
  background: radial-gradient(circle at 88% 50%, ${t.main} 0, ${t.deep} 55%, #12060a 100%); position: relative; }
.ring { position: absolute; right: -60px; top: 75px; width: 480px; height: 480px; border-radius: 50%;
  border: 18px solid ${t.accent}; opacity: .22; }
.ring.r2 { right: 40px; top: 175px; width: 280px; height: 280px; border-width: 10px; opacity: .3; }
.box { position: absolute; left: 90px; top: 0; bottom: 0; display: grid; align-content: center; border-left: 14px solid ${t.accent}; padding-left: 40px; width: 960px; }
.eyebrow { color: ${t.accent}; font-size: 26px; letter-spacing: .2em; margin: 0 0 16px; font-weight: bold; }
h1 { font-size: ${size}px; white-space: nowrap; margin: 0; line-height: 1.05; font-weight: bold; letter-spacing: .02em; }
p { font-size: 50px; margin: 20px 0 0; font-weight: bold; }
.sub { font-size: 30px; color: ${t.soft}; font-weight: normal; margin-top: 18px; }
</style></head><body><div class="ring"></div><div class="ring r2"></div><div class="box">
<div class="eyebrow">${ja ? "MCU 非公式ガイド" : "UNOFFICIAL MCU GUIDE"} · ${esc(o.year)}</div>
<h1>${esc(big)}</h1>
<p>${ja ? "完全ガイド" : "Complete Guide"}</p>
<p class="sub">${ja ? "あらすじ・相関図・用語をやさしく解説" : "Story, character map and key terms, explained simply"}</p>
</div></body></html>`;
}

(async () => {
  const browser = await chromium.launch();
  const page = await browser.newPage({ viewport: { width: 1200, height: 630 } });
  for (const o of JSON.parse(fs.readFileSync(path.join(SRC, "og.json"), "utf8"))) {
    await page.setContent(filmOg(o));
    await page.screenshot({ path: path.join(ROOT, o.out) });
    console.log(o.out);
  }
  await browser.close();
})();
