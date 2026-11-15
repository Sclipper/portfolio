(() => {
  const reduce = window.matchMedia('(prefers-reduced-motion: reduce)').matches;

  /* Masthead hairline once the page moves */
  const head = document.querySelector('.masthead');
  const onScroll = () => head.classList.toggle('is-scrolled', window.scrollY > 8);
  onScroll();
  window.addEventListener('scroll', onScroll, { passive: true });

  /* Current section in the masthead */
  const links = [...document.querySelectorAll('.masthead__nav a')];
  const sections = links.map(a => document.querySelector(a.getAttribute('href'))).filter(Boolean);
  if ('IntersectionObserver' in window) {
    const io = new IntersectionObserver(entries => {
      entries.forEach(e => {
        if (!e.isIntersecting) return;
        links.forEach(a => a.getAttribute('href') === '#' + e.target.id
          ? a.setAttribute('aria-current', 'true')
          : a.removeAttribute('aria-current'));
      });
    }, { rootMargin: '-45% 0px -50% 0px' });
    sections.forEach(s => io.observe(s));
  }

  /* The list of works: a plate follows the pointer */
  const preview = document.querySelector('.preview');
  const fine = window.matchMedia('(hover: hover) and (pointer: fine)').matches;
  if (preview && fine) {
    const img = preview.querySelector('img');
    let x = 0, y = 0, tx = 0, ty = 0, raf = 0, on = false;
    const tick = () => {
      x += (tx - x) * (reduce ? 1 : 0.16);
      y += (ty - y) * (reduce ? 1 : 0.16);
      preview.style.transform = `translate3d(${x}px, ${y}px, 0)`;
      raf = (on || Math.abs(tx - x) > 0.5) ? requestAnimationFrame(tick) : 0;
    };
    const place = e => {
      const w = preview.offsetWidth, h = preview.offsetHeight || w * 0.625;
      // The list sits on the right, so the plate hangs to the left of the pointer
      const list = document.querySelector('.checklist__rows').getBoundingClientRect();
      tx = Math.max(16, list.left - w - 40);
      ty = Math.min(Math.max(e.clientY - h / 2, 16), window.innerHeight - h - 16);
    };
    document.querySelectorAll('.row[data-preview]').forEach(row => {
      row.addEventListener('pointerenter', e => {
        if (img.getAttribute('src') !== row.dataset.preview) img.src = row.dataset.preview;
        place(e);
        if (!on) { x = tx; y = ty; }
        on = true;
        preview.classList.add('is-on');
        if (!raf) raf = requestAnimationFrame(tick);
      });
      row.addEventListener('pointermove', place);
      row.addEventListener('pointerleave', () => { on = false; preview.classList.remove('is-on'); });
    });
    // Warm the cache so the first hover is instant
    const warm = () => document.querySelectorAll('.row[data-preview]').forEach(r => { const i = new Image(); i.src = r.dataset.preview; });
    ('requestIdleCallback' in window) ? requestIdleCallback(warm) : setTimeout(warm, 1500);
  }

  /* Film plates play on request, never on their own */
  document.querySelectorAll('.film').forEach(film => {
    const v = film.querySelector('video');
    const b = film.querySelector('.film__play');
    v.removeAttribute('controls');
    film.classList.add('is-enhanced');
    const play = () => { v.controls = true; v.play().then(() => film.classList.add('is-playing')).catch(() => {}); };
    b.addEventListener('click', play);
    v.addEventListener('pause', () => film.classList.remove('is-playing'));
    if ('IntersectionObserver' in window) {
      new IntersectionObserver(([e]) => { if (!e.isIntersecting && !v.paused) v.pause(); }, { threshold: 0.1 }).observe(v);
    }
  });
})();
