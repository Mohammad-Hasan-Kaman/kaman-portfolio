/* ================================================================
   KAMAN.PORTFOLIO — interactions
   ================================================================ */
(function () {
  'use strict';

  /* ---------------- Theme toggle ---------------- */
  const themeToggle = document.getElementById('themeToggle');
  themeToggle.addEventListener('click', () => {
    const current = document.documentElement.getAttribute('data-theme');
    const next = current === 'dark' ? 'light' : 'dark';
    document.documentElement.setAttribute('data-theme', next);
    localStorage.setItem('theme', next);
  });

  /* ---------------- Language menu ---------------- */
  const langBtn = document.getElementById('langBtn');
  const langMenu = document.querySelector('.lang-menu');
  langBtn.addEventListener('click', (e) => {
    e.stopPropagation();
    langMenu.classList.toggle('open');
  });
  document.addEventListener('click', () => langMenu.classList.remove('open'));

  /* ---------------- Mobile nav ---------------- */
  const hamburger = document.getElementById('hamburger');
  const navLinks = document.getElementById('navLinks');
  hamburger.addEventListener('click', () => {
    hamburger.classList.toggle('open');
    navLinks.classList.toggle('open');
  });
  navLinks.querySelectorAll('a').forEach((a) =>
    a.addEventListener('click', () => {
      hamburger.classList.remove('open');
      navLinks.classList.remove('open');
    })
  );

  /* ---------------- Navbar scroll state ---------------- */
  const navWrap = document.getElementById('navWrap');
  const onScroll = () => navWrap.classList.toggle('scrolled', window.scrollY > 20);
  window.addEventListener('scroll', onScroll, { passive: true });
  onScroll();

  /* ---------------- Typing effect ---------------- */
  const typingEl = document.getElementById('typing');
  if (typingEl) {
    const roles = (typingEl.dataset.roles || '').split('|').filter(Boolean);
    let ri = 0, ci = 0, deleting = false;
    (function type() {
      const word = roles[ri] || '';
      typingEl.textContent = word.slice(0, ci);
      let delay = deleting ? 45 : 95;
      if (!deleting && ci === word.length) { delay = 1800; deleting = true; }
      else if (deleting && ci === 0) { deleting = false; ri = (ri + 1) % roles.length; delay = 350; }
      else ci += deleting ? -1 : 1;
      setTimeout(type, delay);
    })();
  }

  /* ---------------- Scroll reveal ---------------- */
  const io = new IntersectionObserver(
    (entries) => entries.forEach((en) => {
      if (en.isIntersecting) { en.target.classList.add('visible'); io.unobserve(en.target); }
    }),
    { threshold: 0.12 }
  );
  document.querySelectorAll('.reveal').forEach((el) => io.observe(el));

  /* ---------------- Animated counters ---------------- */
  const counterIO = new IntersectionObserver(
    (entries) => entries.forEach((en) => {
      if (!en.isIntersecting) return;
      counterIO.unobserve(en.target);
      const el = en.target;
      const target = parseInt(el.dataset.count, 10) || 0;
      const dur = 1400, start = performance.now();
      (function tick(now) {
        const p = Math.min((now - start) / dur, 1);
        el.textContent = Math.round(target * (1 - Math.pow(1 - p, 3)));
        if (p < 1) requestAnimationFrame(tick);
      })(start);
    }),
    { threshold: 0.6 }
  );
  document.querySelectorAll('.stat-num').forEach((el) => counterIO.observe(el));

  /* ---------------- Skill bars ---------------- */
  // Skill cards now use tier labels (no percent bars) — observer kept for reveal animations only

  /* ---------------- Project filters ---------------- */
  const filterBtns = document.querySelectorAll('.filter-btn');
  filterBtns.forEach((btn) =>
    btn.addEventListener('click', () => {
      filterBtns.forEach((b) => b.classList.remove('active'));
      btn.classList.add('active');
      const f = btn.dataset.filter;
      document.querySelectorAll('[data-category]').forEach((card) => {
        const show = f === 'all' || card.dataset.category === f;
        card.classList.toggle('hidden', !show);
        if (show) card.classList.add('visible');
      });
    })
  );

  /* ---------------- Contact form (AJAX) ---------------- */
  const form = document.getElementById('contactForm');
  if (form) {
    form.addEventListener('submit', async (e) => {
      e.preventDefault();
      const btn = document.getElementById('sendBtn');
      const msg = document.getElementById('formMsg');
      const original = btn.textContent;
      btn.disabled = true;
      msg.className = 'form-msg';
      msg.textContent = form.dataset.sending || '';

      try {
        const res = await fetch(form.action, {
          method: 'POST',
          body: new FormData(form),
          headers: { 'X-Requested-With': 'XMLHttpRequest' },
        });
        // A 403 CSRF page (or any HTML error) is not JSON - show a friendly
        // "refresh the page" message instead of crashing on res.json().
        const ctype = res.headers.get('content-type') || '';
        const data = ctype.includes('json')
          ? await res.json()
          : { ok: false, msg: '⚠ جلسه منقضی شده — صفحه را یک بار رفرش کنید و دوباره بفرستید' };
        msg.textContent = data.msg;
        msg.classList.add(res.ok ? 'ok' : 'err');
        if (res.ok) form.reset();
      } catch {
        msg.className = 'form-msg err';
        msg.textContent = '⚠ Network error';
      } finally {
        btn.disabled = false;
        btn.textContent = original;
      }
    });
  }

  /* ---------------- Scroll progress bar ---------------- */
  const pbar = document.getElementById('progressBar');
  const updateProgress = () => {
    if (!pbar) return;
    const h = document.documentElement;
    const max = h.scrollHeight - h.clientHeight;
    pbar.style.width = (max > 0 ? (h.scrollTop / max) * 100 : 0) + '%';
  };
  window.addEventListener('scroll', updateProgress, { passive: true });
  updateProgress();

  /* ---------------- Cursor tilt + orb parallax (desktop only) ---------------- */
  if (window.matchMedia('(hover: hover)').matches) {
    document.querySelectorAll('.tilt').forEach((el) => {
      el.addEventListener('mousemove', (e) => {
        const r = el.getBoundingClientRect();
        const x = (e.clientX - r.left) / r.width - 0.5;
        const y = (e.clientY - r.top) / r.height - 0.5;
        el.style.transform = `perspective(800px) rotateY(${x * 10}deg) rotateX(${-y * 10}deg)`;
      });
      el.addEventListener('mouseleave', () => { el.style.transform = ''; });
    });

    const orbs = document.querySelectorAll('.orb');
    window.addEventListener('mousemove', (e) => {
      const dx = e.clientX / window.innerWidth - 0.5;
      const dy = e.clientY / window.innerHeight - 0.5;
      orbs.forEach((o, i) => {
        const f = (i + 1) * 14;
        o.style.translate = `${dx * f}px ${dy * f}px`;
      });
    });
  }
})();
