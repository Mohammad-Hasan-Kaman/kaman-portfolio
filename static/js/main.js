// mhkaman.com: theme toggle, mobile nav, project filter, contact form.
// MOTION dial is 1: no entrance animation, no loops. These are state changes only.

(function () {
  // Theme: stored choice wins, otherwise the OS preference, otherwise light.
  // (The pre-paint init in base.html has already applied the theme; this
  // wires the toggle button and keeps the label in sync.)
  var root = document.documentElement;
  var themeBtn = document.querySelector(".theme-btn");
  if (themeBtn) {
    var syncLabel = function () {
      var dark = root.getAttribute("data-theme") === "dark";
      themeBtn.textContent = themeBtn.getAttribute(dark ? "data-label-light" : "data-label-dark");
      themeBtn.setAttribute("aria-pressed", dark ? "true" : "false");
    };
    syncLabel();
    themeBtn.addEventListener("click", function () {
      var next = root.getAttribute("data-theme") === "dark" ? "light" : "dark";
      root.setAttribute("data-theme", next);
      try { localStorage.setItem("mhk-theme", next); } catch (e) {}
      syncLabel();
    });
  }

  // Mobile navigation.
  var toggle = document.querySelector(".nav-toggle");
  var nav = document.querySelector(".main-nav");
  if (toggle && nav) {
    toggle.addEventListener("click", function () {
      var open = nav.classList.toggle("open");
      toggle.setAttribute("aria-expanded", open ? "true" : "false");
    });
    nav.addEventListener("click", function (ev) {
      if (ev.target.closest("a")) {
        nav.classList.remove("open");
        toggle.setAttribute("aria-expanded", "false");
      }
    });
    document.addEventListener("keydown", function (ev) {
      if (ev.key === "Escape" && nav.classList.contains("open")) {
        nav.classList.remove("open");
        toggle.setAttribute("aria-expanded", "false");
        toggle.focus();
      }
    });
  }

  // Project filter: plain buttons, entries carry data-category.
  var filterBtns = document.querySelectorAll(".filters button[data-filter]");
  var entries = document.querySelectorAll("[data-category]");
  filterBtns.forEach(function (btn) {
    btn.addEventListener("click", function () {
      filterBtns.forEach(function (b) { b.setAttribute("aria-pressed", "false"); });
      btn.setAttribute("aria-pressed", "true");
      var f = btn.getAttribute("data-filter");
      entries.forEach(function (el) {
        el.hidden = !(f === "all" || el.getAttribute("data-category") === f);
      });
    });
  });

  // Contact form: posts to the Django handler (portfolio:contact_submit),
  // which answers JSON {ok, msg}. Same behavior as the previous site.
  var form = document.getElementById("contactForm");
  if (form) {
    form.addEventListener("submit", function (ev) {
      ev.preventDefault();
      var btn = document.getElementById("sendBtn");
      var note = document.getElementById("formMsg");
      var original = btn.textContent;
      btn.disabled = true;
      note.className = "form-note";
      note.textContent = form.getAttribute("data-sending") || "";

      fetch(form.action, {
        method: "POST",
        body: new FormData(form),
        headers: { "X-Requested-With": "XMLHttpRequest" }
      }).then(function (res) {
        var ctype = res.headers.get("content-type") || "";
        return ctype.indexOf("json") !== -1
          ? res.json()
          : { ok: false, msg: "⚠ جلسه منقضی شده — صفحه را یک بار رفرش کنید و دوباره بفرستید" };
      }).then(function (data) {
        note.textContent = data.msg || "";
        note.classList.add(data.ok ? "ok" : "err");
        if (data.ok) form.reset();
      }).catch(function () {
        note.className = "form-note err";
        note.textContent = "⚠ Network error";
      }).then(function () {
        btn.disabled = false;
        btn.textContent = original;
      });
    });
  }
})();
