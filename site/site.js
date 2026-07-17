/* Shared behavior: nav, reveals, tilt, scroll progress, counters, dust canvas, FAQ. */
(function () {
  const reduceMotion = window.matchMedia('(prefers-reduced-motion: reduce)').matches;

  /* Theme toggle (theme is applied pre-CSS by an inline head script to avoid flashing) */
  const root = document.documentElement;
  const toggle = document.querySelector('.theme-toggle');
  function setTheme(t) {
    root.dataset.theme = t;
    try { localStorage.setItem('st-theme', t); } catch (e) {}
    if (toggle) {
      toggle.textContent = t === 'light' ? '🌙' : '☀️';
      toggle.setAttribute('aria-label', t === 'light' ? 'Switch to dark theme' : 'Switch to light theme');
    }
    window.dispatchEvent(new CustomEvent('st-theme', { detail: t }));
  }
  if (toggle) {
    toggle.textContent = root.dataset.theme === 'light' ? '🌙' : '☀️';
    toggle.setAttribute('aria-label', root.dataset.theme === 'light' ? 'Switch to dark theme' : 'Switch to light theme');
    toggle.addEventListener('click', () => {
      setTheme(root.dataset.theme === 'light' ? 'dark' : 'light');
    });
  }

  /* Mobile menu */
  const burger = document.querySelector('.nav-burger');
  const menu = document.querySelector('.mobile-menu');
  if (burger && menu) {
    burger.addEventListener('click', () => {
      const open = menu.classList.toggle('open');
      burger.setAttribute('aria-expanded', open);
      burger.textContent = open ? '✕' : '☰';
    });
    menu.querySelectorAll('a').forEach(a => a.addEventListener('click', () => {
      menu.classList.remove('open');
      burger.textContent = '☰';
    }));
  }

  /* Scroll progress bar */
  const bar = document.getElementById('scroll-progress');
  if (bar) {
    const update = () => {
      const max = document.documentElement.scrollHeight - innerHeight;
      bar.style.width = (max > 0 ? (scrollY / max) * 100 : 0) + '%';
    };
    addEventListener('scroll', update, { passive: true });
    update();
  }

  /* Reveal on scroll */
  const io = new IntersectionObserver((entries) => {
    entries.forEach(e => { if (e.isIntersecting) { e.target.classList.add('in'); io.unobserve(e.target); } });
  }, { threshold: 0.15 });
  document.querySelectorAll('.reveal').forEach(el => io.observe(el));

  /* Count-up stats */
  const ioStats = new IntersectionObserver((entries) => {
    entries.forEach(e => {
      if (!e.isIntersecting) return;
      ioStats.unobserve(e.target);
      const el = e.target, target = +el.dataset.count, suffix = el.dataset.suffix || '';
      const start = performance.now();
      (function step(now) {
        const k = Math.min((now - start) / 1400, 1);
        const eased = 1 - Math.pow(1 - k, 3);
        el.textContent = Math.round(target * eased) + (k === 1 ? suffix : '');
        if (k < 1) requestAnimationFrame(step);
      })(start);
    });
  }, { threshold: 0.4 });
  document.querySelectorAll('[data-count]').forEach(el => ioStats.observe(el));

  /* Card 3D tilt + glow position */
  document.querySelectorAll('.tilt').forEach(card => {
    card.addEventListener('pointermove', (e) => {
      const r = card.getBoundingClientRect();
      const x = (e.clientX - r.left) / r.width, y = (e.clientY - r.top) / r.height;
      card.style.setProperty('--mx', (x * 100) + '%');
      card.style.setProperty('--my', (y * 100) + '%');
      if (!reduceMotion) {
        card.style.transform = `perspective(900px) rotateY(${(x - 0.5) * 7}deg) rotateX(${(0.5 - y) * 7}deg) translateY(-3px)`;
      }
    });
    card.addEventListener('pointerleave', () => { card.style.transform = ''; });
  });

  /* FAQ accordion */
  document.querySelectorAll('.faq-item').forEach(item => {
    const q = item.querySelector('.faq-q');
    const a = item.querySelector('.faq-a');
    q.addEventListener('click', () => {
      const open = item.classList.toggle('open');
      a.style.maxHeight = open ? a.scrollHeight + 'px' : '0px';
    });
  });

  /* Lightweight "story dust" canvas for subpage heroes (2D, cheap) */
  document.querySelectorAll('canvas.dust').forEach(canvas => {
    const ctx = canvas.getContext('2d');
    let w, h, parts;
    const COLORS = ['rgba(160,124,255,', 'rgba(255,122,217,', 'rgba(110,193,255,'];
    function resize() {
      w = canvas.width = canvas.offsetWidth * devicePixelRatio;
      h = canvas.height = canvas.offsetHeight * devicePixelRatio;
    }
    function init() {
      parts = Array.from({ length: 90 }, () => ({
        x: Math.random() * w, y: Math.random() * h,
        r: (Math.random() * 1.6 + 0.4) * devicePixelRatio,
        vx: (Math.random() - 0.5) * 0.12 * devicePixelRatio,
        vy: (Math.random() - 0.5) * 0.12 * devicePixelRatio,
        c: COLORS[(Math.random() * 3) | 0],
        a: Math.random() * 0.5 + 0.15,
        p: Math.random() * Math.PI * 2,
      }));
    }
    resize(); init();
    addEventListener('resize', () => { resize(); init(); });
    (function tick(t) {
      ctx.clearRect(0, 0, w, h);
      for (const p of parts) {
        p.x = (p.x + p.vx + w) % w;
        p.y = (p.y + p.vy + h) % h;
        const tw = reduceMotion ? 1 : (0.6 + 0.4 * Math.sin(t / 900 + p.p));
        ctx.beginPath();
        ctx.arc(p.x, p.y, p.r, 0, Math.PI * 2);
        ctx.fillStyle = p.c + (p.a * tw) + ')';
        ctx.fill();
      }
      if (!reduceMotion) requestAnimationFrame(tick);
    })(0);
  });
})();
