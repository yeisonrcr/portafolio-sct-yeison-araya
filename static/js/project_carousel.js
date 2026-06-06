/**
 * project_carousel.js — Carrusel horizontal infinito.
 * Funciona con GSAP o con CSS puro como fallback.
 * Soporta drag/swipe en móvil y desktop.
 */

(function () {
  'use strict';

  document.addEventListener('DOMContentLoaded', () => {
    const carousel = document.getElementById('projectCarousel');
    const prevBtn  = document.getElementById('carouselPrev');
    const nextBtn  = document.getElementById('carouselNext');

    if (!carousel) return;

    const CARD_WIDTH   = 360; // width + gap aprox
    let   currentIndex = 0;
    let   isDragging   = false;
    let   startX       = 0;
    let   scrollLeft   = 0;
    let   autoTimer    = null;

    const cards = carousel.querySelectorAll('.project-card');
    const total = Math.ceil(cards.length / 2); // mitad real (la otra es clon)

    // ─── Función de scroll suave ──────────────────────
    const scrollTo = (index, animated = true) => {
      const target = index * CARD_WIDTH;
      if (typeof gsap !== 'undefined' && animated) {
        gsap.to(carousel, {
          scrollLeft: target,
          duration: 0.6,
          ease: 'power2.inOut',
        });
      } else {
        carousel.scrollLeft = target;
      }
    };

    // ─── Next / Prev ──────────────────────────────────
    const next = () => {
      currentIndex++;
      if (currentIndex >= total) {
        // Salto invisible al principio
        carousel.scrollLeft = 0;
        currentIndex = 1;
      }
      scrollTo(currentIndex);
    };

    const prev = () => {
      if (currentIndex <= 0) {
        // Salto invisible al final
        carousel.scrollLeft = total * CARD_WIDTH;
        currentIndex = total - 1;
      } else {
        currentIndex--;
      }
      scrollTo(currentIndex);
    };

    if (nextBtn) nextBtn.addEventListener('click', next);
    if (prevBtn) prevBtn.addEventListener('click', prev);

    // ─── Auto-play ────────────────────────────────────
    const startAuto = () => {
      autoTimer = setInterval(next, 4000);
    };

    const stopAuto = () => clearInterval(autoTimer);

    startAuto();
    carousel.addEventListener('mouseenter', stopAuto);
    carousel.addEventListener('mouseleave', startAuto);

    // ─── Drag (mouse) ─────────────────────────────────
    carousel.addEventListener('mousedown', e => {
      isDragging = true;
      startX     = e.pageX - carousel.offsetLeft;
      scrollLeft = carousel.scrollLeft;
      carousel.style.cursor = 'grabbing';
    });

    carousel.addEventListener('mousemove', e => {
      if (!isDragging) return;
      e.preventDefault();
      const x    = e.pageX - carousel.offsetLeft;
      const walk = (x - startX) * 1.5;
      carousel.scrollLeft = scrollLeft - walk;
    });

    const endDrag = () => {
      isDragging = false;
      carousel.style.cursor = 'grab';
      // Snap al card más cercano
      const nearest = Math.round(carousel.scrollLeft / CARD_WIDTH);
      currentIndex  = Math.max(0, Math.min(nearest, total - 1));
      scrollTo(currentIndex);
    };

    carousel.addEventListener('mouseup',    endDrag);
    carousel.addEventListener('mouseleave', endDrag);

    // ─── Touch (móvil) ────────────────────────────────
    let touchStartX = 0;

    carousel.addEventListener('touchstart', e => {
      touchStartX = e.touches[0].clientX;
      stopAuto();
    }, { passive: true });

    carousel.addEventListener('touchend', e => {
      const delta = touchStartX - e.changedTouches[0].clientX;
      if (Math.abs(delta) > 50) {
        delta > 0 ? next() : prev();
      } else {
        endDrag();
      }
      startAuto();
    }, { passive: true });

    // ─── Keyboard ─────────────────────────────────────
    document.addEventListener('keydown', e => {
      if (e.key === 'ArrowRight') next();
      if (e.key === 'ArrowLeft')  prev();
    });
  });

})();
