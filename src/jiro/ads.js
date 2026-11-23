// ============================================================
// 広告設定（Google AdSense）
// AdSense の審査に通ったら、下の client と slots を埋めるだけで
// サイト内のすべての広告枠に本物の広告が出ます。
// 空のままの間は「広告枠」というダミーの箱が表示されます。
// ============================================================
const ADS = {
  client: "ca-pub-8047459455202561",   // アドセンスの読み込みタグは index.html の head に入れてある
  showDummy: false,      // true にすると、中身のない広告枠を「広告枠」という箱で表示する（確認用）
  amazonTag: "doomsdayguide-22",      // Amazon アソシエイト。PR リンクに使う
  slots: {
    top: "",             // ページ上部の横長バナー
    infeed: "",          // 店舗一覧の途中に挟まる広告
    middle: "",          // 一覧とコラムの間
    bottom: "",          // ページ下部
    side: "",            // 右サイドバー（縦長・四角）
  },

  // ---- ×ボタンで閉じる大きい画像広告（全画面ポップアップ）----
  // image と link にアフィリエイト（A8.net・もしも等）のバナー画像URLとリンク先を入れる。
  // 空のままだとダミー画像が出ます。
  // ※ AdSense の広告をこの中に入れるのは規約違反なので、ここは画像バナー専用です。
  popup: {
    enabled: true,
    image: "",           // 例: "https://example.com/banner-600x500.jpg"
    link: "",            // 例: "https://px.a8.net/..."
    delaySeconds: 3,     // ページを開いて何秒後に出すか
    closeAfterSeconds: 2,// ×ボタンが押せるようになるまでの秒数（0ですぐ押せる）
    everyMinutes: 30,    // 一度閉じたら何分間は出さないか（0で毎回出す）
  },

  // ---- 画面下に張り付く横長バナー（×で閉じる）----
  sticky: {
    enabled: true,
    image: "",           // 例: 横長 728x90 / 320x100 のバナー画像URL
    link: "",
  },
};

// ×で閉じる広告（ポップアップ・下部固定バナー）
(function () {
  const css = `
  .adpop { position: fixed; inset: 0; z-index: 1000; background: rgba(0,0,0,.72);
    display: grid; place-items: center; padding: 16px; animation: adfade .25s; }
  @keyframes adfade { from { opacity: 0 } }
  .adpop-inner { position: relative; max-width: min(640px, 100%); }
  .adpop-inner a { display: block; }
  .adpop img, .adpop .adpop-dummy { display: block; max-width: 100%; max-height: 78vh; border-radius: 10px;
    box-shadow: 0 10px 40px rgba(0,0,0,.5); }
  .adpop .adpop-dummy { width: 600px; aspect-ratio: 6/5; background: #f3ecd8; border: 3px dashed #bdb39a;
    display: grid; place-items: center; color: #8c8370; font-weight: 700; font-size: 20px; text-align: center; }
  .adpop-tag { position: absolute; left: 8px; top: 8px; background: rgba(0,0,0,.6); color: #fff;
    font-size: 11px; padding: 1px 8px; border-radius: 3px; }
  .ad-x { position: absolute; right: -10px; top: -14px; width: 44px; height: 44px; border-radius: 50%;
    border: 3px solid #fff; background: #161310; color: #fff; font-size: 24px; font-weight: 700; line-height: 1;
    cursor: pointer; display: grid; place-items: center; box-shadow: 0 2px 8px rgba(0,0,0,.4); }
  .ad-x:disabled { font-size: 15px; opacity: .85; cursor: default; }
  .adsticky { position: fixed; left: 0; right: 0; bottom: 0; z-index: 900; background: rgba(255,255,255,.96);
    border-top: 2px solid #161310; padding: 6px 12px; display: flex; justify-content: center; }
  .adsticky-inner { position: relative; }
  .adsticky img, .adsticky .adsticky-dummy { display: block; max-width: 100%; height: auto; max-height: 100px; }
  .adsticky .adsticky-dummy { width: min(728px, 86vw); height: 90px; background: #f3ecd8; border: 2px dashed #bdb39a;
    display: grid; place-items: center; color: #8c8370; font-weight: 700; }
  .adsticky .ad-x { width: 30px; height: 30px; font-size: 16px; border-width: 2px; right: -8px; top: -18px; }
  body.has-sticky { padding-bottom: 116px; }`;
  const st = document.createElement("style");
  st.textContent = css;
  document.head.appendChild(st);

  const KEY = "ad-pop-closed";
  const media = (cfg, dummyClass, dummyText) => {
    const body = cfg.image
      ? '<img src="' + cfg.image + '" alt="広告">'
      : '<div class="' + dummyClass + '">' + dummyText + "</div>";
    return cfg.link ? '<a href="' + cfg.link + '" target="_blank" rel="sponsored noopener">' + body + "</a>" : body;
  };

  function showPopup() {
    const p = ADS.popup;
    const el = document.createElement("div");
    el.className = "adpop";
    el.innerHTML = '<div class="adpop-inner">' +
      media(p, "adpop-dummy", "広告画像（大）<br>ads.js の popup.image に画像URLを入れる") +
      '<span class="adpop-tag">広告</span>' +
      '<button class="ad-x" aria-label="広告を閉じる">×</button></div>';
    document.body.appendChild(el);
    const x = el.querySelector(".ad-x");
    const close = () => {
      el.remove();
      try { localStorage.setItem(KEY, String(Date.now())); } catch (e) {}
    };
    let left = p.closeAfterSeconds || 0;
    const tick = () => {
      if (left <= 0) { x.disabled = false; x.textContent = "×"; return; }
      x.disabled = true; x.textContent = left; left--; setTimeout(tick, 1000);
    };
    tick();
    x.addEventListener("click", close);
    // 画像の外側（暗い部分）を押しても閉じる
    el.addEventListener("click", e => { if (e.target === el && !x.disabled) close(); });
  }

  function showSticky() {
    const el = document.createElement("div");
    el.className = "adsticky";
    el.innerHTML = '<div class="adsticky-inner">' +
      media(ADS.sticky, "adsticky-dummy", "広告枠（下部固定バナー）") +
      '<button class="ad-x" aria-label="広告を閉じる">×</button></div>';
    document.body.appendChild(el);
    document.body.classList.add("has-sticky");
    el.querySelector(".ad-x").addEventListener("click", () => {
      el.remove(); document.body.classList.remove("has-sticky");
    });
  }

  window.addEventListener("DOMContentLoaded", function () {
    if (ADS.sticky && ADS.sticky.enabled && (ADS.sticky.image || ADS.showDummy)) showSticky();
    if (ADS.popup && ADS.popup.enabled && (ADS.popup.image || ADS.showDummy)) {
      let last = 0;
      try { last = Number(localStorage.getItem(KEY) || 0); } catch (e) {}
      const wait = (ADS.popup.everyMinutes || 0) * 60000;
      if (!wait || Date.now() - last > wait) setTimeout(showPopup, (ADS.popup.delaySeconds || 0) * 1000);
    }
  });
})();

(function () {
  const live = ADS.client && ADS.client.startsWith("ca-pub-");
  if (false) {
    const s = document.createElement("script");
    s.async = true;
    s.crossOrigin = "anonymous";
    s.src = "https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js?client=" + ADS.client;
    document.head.appendChild(s);
  }

  // Amazon の検索結果へ送る PR リンク（場所ごと）
  const PR_LINKS = {
    middle: { q: "二郎系 ラーメン お取り寄せ", text: "家で食べられる二郎系ラーメン（お取り寄せ・冷凍）を Amazon で探す", sub: "店に行けない日のために。極太麺と豚がセットになった商品があります。" },
    bottom: { q: "二郎系 カップ麺", text: "二郎系のカップ麺を Amazon で探す", sub: "コンビニで見つからない商品も、まとめ買いできます。" },
  };

  // <div class="ad" data-ad="top"></div> を広告に置き換える
  window.fillAds = function (root) {
    (root || document).querySelectorAll(".ad:not([data-filled])").forEach(function (el) {
      el.dataset.filled = "1";
      const slot = ADS.slots[el.dataset.ad];
      if (live && slot) {
        el.innerHTML =
          '<span class="ad-label">スポンサーリンク</span>' +
          '<ins class="adsbygoogle" style="display:block" data-ad-client="' + ADS.client +
          '" data-ad-slot="' + slot + '" data-ad-format="auto" data-full-width-responsive="true"></ins>';
        (window.adsbygoogle = window.adsbygoogle || []).push({});
      } else if (PR_LINKS[el.dataset.ad] && ADS.amazonTag) {
        // アドセンスの枠がまだない場所には、Amazon の PR リンクを出す
        const pr = PR_LINKS[el.dataset.ad];
        const url = "https://www.amazon.co.jp/s?k=" + encodeURIComponent(pr.q) + "&tag=" + ADS.amazonTag;
        el.innerHTML = '<div class="pr-box"><b class="pr">PR</b><a href="' + url + '" target="_blank" rel="sponsored noopener">' + pr.text + '</a><p>' + pr.sub + '</p></div>';
      } else if (ADS.showDummy) {
        el.classList.add("ad-dummy");
        el.innerHTML = '<span class="ad-label">スポンサーリンク</span><div class="ad-box">広告枠（' + el.dataset.ad + '）</div>';
      }
    });
  };
})();
