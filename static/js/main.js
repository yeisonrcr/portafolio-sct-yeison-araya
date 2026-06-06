/**
 * main.js — Comportamientos generales del sitio.
 * Sin dependencias externas. GSAP se maneja en gsap_animations.js
 */

document.addEventListener('DOMContentLoaded', () => {

  // ─── Navbar: scroll effect ──────────────────────────
  const navbar = document.getElementById('navbar');
  if (navbar) {
    const onScroll = () => {
      navbar.classList.toggle('scrolled', window.scrollY > 40);
    };
    window.addEventListener('scroll', onScroll, { passive: true });
    onScroll();
  }

  // ─── Navbar: mobile toggle ��─────────────────────────
  const toggle  = document.getElementById('navToggle');
  const navMenu = document.getElementById('navMenu');

  if (toggle && navMenu) {
    // Crear overlay
    const overlay = document.createElement('div');
    overlay.className = 'nav-overlay';
    document.body.appendChild(overlay);

    const openNav = () => {
      navMenu.classList.add('open');
      overlay.classList.add('active');
      document.body.style.overflow = 'hidden';
      toggle.setAttribute('aria-expanded', 'true');
    };

    const closeNav = () => {
      navMenu.classList.remove('open');
      overlay.classList.remove('active');
      document.body.style.overflow = '';
      toggle.setAttribute('aria-expanded', 'false');
    };

    toggle.addEventListener('click', () => {
      navMenu.classList.contains('open') ? closeNav() : openNav();
    });

    overlay.addEventListener('click', closeNav);

    navMenu.querySelectorAll('.navbar__link').forEach(link => {
      link.addEventListener('click', closeNav);
    });

    // ESC key
    document.addEventListener('keydown', (e) => {
      if (e.key === 'Escape') closeNav();
    });
  }

  // ─── Navbar: active link ───────��────────────────────
  const currentPath = window.location.pathname;
  document.querySelectorAll('.navbar__link').forEach(link => {
    const href = link.getAttribute('href');
    if (href && href !== '/' && currentPath.startsWith(href)) {
      link.classList.add('active');
    } else if (href === '/' && currentPath === '/') {
      link.classList.add('active');
    }
  });

  // ─── Auto-dismiss messages ──────────────────────────
  const messages = document.querySelectorAll('.message');
  messages.forEach(msg => {
    setTimeout(() => {
      msg.style.opacity = '0';
      msg.style.transform = 'translateX(100%)';
      msg.style.transition = 'all 0.4s ease';
      setTimeout(() => msg.remove(), 400);
    }, 5000);
  });

});
