// パラダイスシティ情報サイトの動き：キャンペーンの期限表示、予算シミュレーター、記事の絞り込み、サイト内検索、FAQの一括開閉
(function () {
  const $ = (sel, root) => (root || document).querySelector(sel);
  const $$ = (sel, root) => [...(root || document).querySelectorAll(sel)];
  const today = new Date();
  today.setHours(0, 0, 0, 0);
  const parse = (s) => (s ? new Date(s + "T00:00:00+09:00") : null);
  const yen = (n) => Math.floor(n).toLocaleString("ja-JP");
  const esc = (s) => String(s).replace(/[&<>"]/g, (c) => ({ "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;" }[c]));

  // キャンペーン：data-end（宿泊・予約の最終日）を過ぎたら「終了」、まだなら残り日数を出す
  $$("[data-campaign]").forEach((el) => {
    const end = parse(el.dataset.end);
    const start = parse(el.dataset.start);
    const state = $(".state", el);
    if (!state || !end) return;
    const days = Math.round((end - today) / 86400000);
    if (days < 0) {
      state.textContent = "終了";
      state.className = "state state-ended";
      el.classList.add("is-past");
    } else if (start && start > today) {
      state.textContent = "予約開始前";
      state.className = "state state-unknown";
    } else {
      state.textContent = days === 0 ? "本日まで" : `あと${days}日`;
      state.className = "state state-open";
    }
  });

  // 予算シミュレーター（参考の目安。利益を約束するものではない）
  const sim = $("#sim");
  if (sim) {
    const budget = $("#sim-budget");
    const bet = $("#sim-bet");
    const hours = $("#sim-hours");
    const out = $("#sim-out");
    const render = () => {
      const b = Math.max(0, Number(budget.value) || 0);
      const m = Math.max(1, Number(bet.value) || 1);
      const h = Math.max(1, Number(hours.value) || 1);
      const units = Math.floor(b / m);
      let level, tips;
      if (units < 1) {
        level = "最低ベットに届いていません";
        tips = ["この金額ではテーブルに座れない可能性があります。見学やルールの確認から始めましょう。"];
      } else if (units < 7) {
        level = "かなり少なめ：数回の負けで終わる金額です";
        tips = ["ルールに慣れるための「体験」と割り切りましょう。", "取り返そうとして追加で両替しないことを先に決めておきましょう。"];
      } else if (units < 20) {
        level = "少なめ：短い時間なら遊べる目安です";
        tips = ["1回の賭け金は最低ベットのままにしておきましょう。", "半分まで減ったら、いったん休憩するルールを決めておきましょう。"];
      } else if (units < 50) {
        level = "初心者が落ち着いて遊べる目安です";
        tips = ["1回の賭け金は予算の5%以下を目安にすると、減り方がゆるやかになります。", "時間を区切って、休憩をはさみながら遊びましょう。"];
      } else {
        level = "余裕のある予算です";
        tips = ["余裕があっても、最初に決めた上限は変えないようにしましょう。", "勝っても負けても、終わる時間を先に決めておきましょう。"];
      }
      const perHour = Math.floor(b / h);
      const stop = Math.floor(b / 2);
      const maxBet = Math.max(m, Math.floor(b * 0.05 / 1000) * 1000);
      out.innerHTML = `
        <p class="muted">最低ベット ${yen(m)}円 で</p>
        <p class="sim-big">${yen(units)}回分</p>
        <p class="sim-level">${esc(level)}</p>
        <ul>
          <li>1時間あたりに使ってよい金額の目安：${yen(perHour)}円</li>
          <li>休憩するライン（予算の半分）：残り ${yen(stop)}円 になったら一度席を立つ</li>
          <li>1回の賭け金の上限の目安（予算の5%）：${yen(maxBet)}円</li>
          ${tips.map((t) => `<li>${esc(t)}</li>`).join("")}
        </ul>
        <p class="muted">これは資金管理の目安です。カジノで利益が出ることを示すものではありません。予算は「なくなっても困らない金額」だけにしてください。</p>`;
    };
    [budget, bet, hours].forEach((i) => i.addEventListener("input", render));
    render();
  }

  // 記事のカテゴリー絞り込み
  const chips = $$("[data-filter]");
  if (chips.length) {
    const items = $$("[data-category]");
    chips.forEach((c) => c.addEventListener("click", () => {
      chips.forEach((x) => x.setAttribute("aria-pressed", String(x === c)));
      items.forEach((it) => { it.hidden = c.dataset.filter !== "all" && it.dataset.category !== c.dataset.filter; });
    }));
  }

  // FAQ をまとめて開く・閉じる
  const toggleAll = $("#faq-toggle");
  if (toggleAll) {
    toggleAll.addEventListener("click", () => {
      const all = $$(".faq details");
      const open = !all.every((d) => d.open);
      all.forEach((d) => (d.open = open));
      toggleAll.textContent = open ? "すべて閉じる" : "すべて開く";
    });
    // ページ内リンク（#faq-3 など）で来たら開く
    const target = location.hash && document.getElementById(location.hash.slice(1));
    if (target && target.tagName === "DETAILS") target.open = true;
  }

  // サイト内検索（search.json を読み込んで、ページ内の見出しと文章から探す）
  const results = $("#search-results");
  if (results) {
    const q = new URLSearchParams(location.search).get("q") || "";
    const input = $("#search-page-input");
    if (input) input.value = q;
    const run = (data, query) => {
      const words = query.trim().toLowerCase().split(/\s+/).filter(Boolean);
      if (!words.length) { results.innerHTML = '<li class="muted">キーワードを入れて検索してください。例：食事券、パスポート、ハイアット</li>'; return; }
      const hits = data.filter((d) => words.every((w) => (d.title + " " + d.text).toLowerCase().includes(w)));
      const mark = (s) => { let r = esc(s); words.forEach((w) => { r = r.replace(new RegExp(w.replace(/[.*+?^${}()|[\]\\]/g, "\\$&"), "gi"), (m) => `<mark>${m}</mark>`); }); return r; };
      results.innerHTML = hits.length
        ? hits.map((d) => {
            const i = d.text.toLowerCase().indexOf(words[0]);
            const snip = d.text.slice(Math.max(0, i - 40), Math.max(0, i - 40) + 140);
            return `<li><a href="${esc(d.url)}"><strong>${mark(d.title)}</strong></a><p class="muted">${esc(d.page)}</p><p>${mark(snip)}…</p></li>`;
          }).join("")
        : `<li class="muted">「${esc(query)}」に一致する情報は見つかりませんでした。別の言葉で試してください。</li>`;
    };
    fetch("search.json").then((r) => r.json()).then((data) => run(data, q)).catch(() => {
      results.innerHTML = '<li class="muted">検索データを読み込めませんでした。ページを再読み込みしてください。</li>';
    });
  }
})();
