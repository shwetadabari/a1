/* RISOTTO GARDEN HEARTH & ATELIER - MAIN ENTRY POINT
   Fully synchronized with script.js (Rule 11)
*/

document.addEventListener('DOMContentLoaded', () => {
  // Mobile Drawer Toggle
  const hamburger = document.getElementById('rg-hamburger');
  const drawer = document.getElementById('mobile-drawer');
  const backdrop = document.getElementById('mobile-drawer-backdrop');
  const closeBtn = document.getElementById('mobile-drawer-close');

  const openDrawer = () => {
    if (drawer) drawer.classList.add('active');
    if (backdrop) backdrop.classList.add('active');
    document.body.style.overflow = 'hidden';
  };

  const closeDrawer = () => {
    if (drawer) drawer.classList.remove('active');
    if (backdrop) backdrop.classList.remove('active');
    document.body.style.overflow = '';
  };

  if (hamburger) hamburger.addEventListener('click', openDrawer);
  if (closeBtn) closeBtn.addEventListener('click', closeDrawer);
  if (backdrop) backdrop.addEventListener('click', closeDrawer);

  document.querySelectorAll('.mobile-nav-link').forEach(link => {
    link.addEventListener('click', closeDrawer);
  });

  // Accordion Logic
  const accordionHeaders = document.querySelectorAll('.rg-accordion-header');
  accordionHeaders.forEach(header => {
    header.addEventListener('click', () => {
      const item = header.parentElement;
      const isActive = item.classList.contains('active');
      
      const siblingGroup = item.parentElement.querySelectorAll('.rg-accordion-item');
      siblingGroup.forEach(sibling => sibling.classList.remove('active'));
      
      if (!isActive) {
        item.classList.add('active');
      }
    });
  });

  // Reservation Form Feedback
  const form = document.getElementById('rg-contact-form');
  if (form) {
    form.addEventListener('submit', (e) => {
      e.preventDefault();
      const btn = form.querySelector('button[type="submit"]');
      btn.disabled = true;
      btn.innerHTML = 'Transmitting Reservation Request...';
      
      setTimeout(() => {
        btn.innerHTML = 'Table Reservation Request Received ✓';
        btn.style.backgroundColor = '#52796f';
        const msg = document.createElement('div');
        msg.style.marginTop = '16px';
        msg.style.padding = '14px';
        msg.style.background = 'rgba(82, 121, 111, 0.12)';
        msg.style.border = '1px solid #52796f';
        msg.style.borderRadius = '6px';
        msg.style.color = '#1c1815';
        msg.style.fontSize = '0.9rem';
        msg.innerHTML = '<strong>Hearthmaster Confirmation:</strong> Thank you. Our Seattle dining concierge will contact you within 4 business hours to finalize seating and dietary preferences.';
        form.appendChild(msg);
        form.reset();
      }, 700);
    });
  }
});
