/**
 * gsap_animations.js — Todas las animaciones GSAP.
 * Cargado con defer; se ejecuta después de que el DOM esté listo.
 * GSAP y ScrollTrigger se cargan desde CDN en base.html.
 */

document.addEventListener('DOMContentLoaded', () => {
  // Esperar a que GSAP esté disponible
  if (typeof gsap === 'undefined') return;

  // Registrar plugin
  if (typeof ScrollTrigger !== 'undefined') {
    gsap.registerPlugin(ScrollTrigger);
  }

  // ─── Hero animation ──────────────────────────────────
  const heroPreTitle = document.getElementById('heroPreTitle');
  const heroTitle    = document.getElementById('heroTitle');
  const heroSubtitle = document.getElementById('heroSubtitle');
  const heroDesc     = document.getElementById('heroDesc');
  const heroActions  = document.getElementById('heroActions');
  const heroVisual   = document.getElementById('heroVisual');

  if (heroTitle) {
    const tl = gsap.timeline({ defaults: { ease: 'power3.out' } });

    tl.from(heroPreTitle, { y: 20, opacity: 0, duration: 0.6 })
      .from(heroTitle,    { y: 60, opacity: 0, duration: 0.9 }, '-=0.3')
      .from(heroSubtitle, { y: 30, opacity: 0, duration: 0.7 }, '-=0.5')
      .from(heroDesc,     { y: 20, opacity: 0, duration: 0.6 }, '-=0.4')
      .from(heroActions,  { y: 20, opacity: 0, duration: 0.6 }, '-=0.3');

    if (heroVisual) {
      tl.from(heroVisual, { x: 60, opacity: 0, duration: 0.9, ease: 'power2.out' }, '-=0.8');
    }
  }

  // ─── ScrollTrigger: fade-up ───────────────────────────
  if (typeof ScrollTrigger !== 'undefined') {

    gsap.utils.toArray('[data-gsap="fade-up"]').forEach(el => {
      gsap.to(el, {
        y: 0,
        opacity: 1,
        duration: 0.8,
        ease: 'power2.out',
        scrollTrigger: {
          trigger: el,
          start: 'top 88%',
          toggleActions: 'play none none none',
        },
      });
    });

    gsap.utils.toArray('[data-gsap="slide-right"]').forEach(el => {
      gsap.to(el, {
        x: 0,
        opacity: 1,
        duration: 0.9,
        ease: 'power2.out',
        scrollTrigger: {
          trigger: el,
          start: 'top 85%',
          toggleActions: 'play none none none',
        },
      });
    });

    gsap.utils.toArray('[data-gsap="slide-left"]').forEach(el => {
      gsap.to(el, {
        x: 0,
        opacity: 1,
        duration: 0.9,
        ease: 'power2.out',
        scrollTrigger: {
          trigger: el,
          start: 'top 85%',
          toggleActions: 'play none none none',
        },
      });
    });

    // Stagger en grids de cards
    const grids = document.querySelectorAll('.projects-grid, .blog-grid, .cases-grid, .process-steps');
    grids.forEach(grid => {
      const cards = grid.querySelectorAll(
        '.project-card, .blog-card, .case-card, .case-full, .process-step'
      );
      if (!cards.length) return;
      gsap.from(cards, {
        y: 40,
        opacity: 0,
        duration: 0.6,
        stagger: 0.1,
        ease: 'power2.out',
        scrollTrigger: {
          trigger: grid,
          start: 'top 85%',
          toggleActions: 'play none none none',
        },
      });
    });

    // Quote section
    const quote = document.querySelector('.quote');
    if (quote) {
      gsap.from(quote, {
        y: 30,
        opacity: 0,
        duration: 1,
        ease: 'power2.out',
        scrollTrigger: {
          trigger: quote,
          start: 'top 85%',
        },
      });
    }
  }

  // ─── Custom cursor (solo desktop) ────────────────────
  if (window.matchMedia('(pointer: fine)').matches) {
    const dot  = document.createElement('div');
    const ring = document.createElement('div');
    dot.className  = 'cursor-dot';
    ring.className = 'cursor-ring';
    document.body.appendChild(dot);
    document.body.appendChild(ring);

    let mouseX = 0, mouseY = 0;
    let ringX  = 0, ringY  = 0;

    window.addEventListener('mousemove', e => {
      mouseX = e.clientX;
      mouseY = e.clientY;
      gsap.to(dot, { x: mouseX, y: mouseY, duration: 0.1 });
    });

    const animate = () => {
      ringX += (mouseX - ringX) * 0.12;
      ringY += (mouseY - ringY) * 0.12;
      gsap.set(ring, { x: ringX, y: ringY });
      requestAnimationFrame(animate);
    };
    animate();

    // Hover en links/buttons
    document.querySelectorAll('a, button').forEach(el => {
      el.addEventListener('mouseenter', () => {
        gsap.to(ring, { scale: 2, opacity: 0.6, duration: 0.3 });
        gsap.to(dot,  { scale: 0, duration: 0.3 });
      });
      el.addEventListener('mouseleave', () => {
        gsap.to(ring, { scale: 1, opacity: 1, duration: 0.3 });
        gsap.to(dot,  { scale: 1, duration: 0.3 });
      });
    });
  }

});
