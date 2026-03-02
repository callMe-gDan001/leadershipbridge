  t
document.querySelectorAll('a[href^="#"]').forEach(a=>{
  a.addEventListener('click', e=>{
    e.preventDefault();
    const id = a.getAttribute('href').slice(1);
    const el = document.getElementById(id);
    if (el) el.scrollIntoView({behavior:'smooth'});
  });
});


document.addEventListener('DOMContentLoaded', ()=>{
  const elems = document.querySelectorAll('[data-target]');
  elems.forEach(el=>{
    const target = el.getAttribute('data-target');
  
    if (/^\d+$/.test(target)) {
      let i = 0;
      const to = parseInt(target,10);
      const step = Math.max(1, Math.floor(to/60));
      const iv = setInterval(()=>{
        i += step;
        if (i >= to) { el.textContent = to; clearInterval(iv); }
        else el.textContent = i;
      }, 20);
    }
  });
});
