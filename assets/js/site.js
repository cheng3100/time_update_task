(() => {
  const storageKey = 'site-lang';
  const toggle = document.getElementById('langToggle');
  let lang = localStorage.getItem(storageKey) || 'zh';

  function applyLanguage() {
    document.documentElement.lang = lang === 'zh' ? 'zh-CN' : 'en';
    document.querySelectorAll('.lang.zh').forEach((el) => { el.hidden = lang !== 'zh'; });
    document.querySelectorAll('.lang.en').forEach((el) => { el.hidden = lang !== 'en'; });
    if (toggle) toggle.textContent = lang === 'zh' ? 'English' : '中文';
    localStorage.setItem(storageKey, lang);
  }

  if (toggle) {
    toggle.addEventListener('click', () => {
      lang = lang === 'zh' ? 'en' : 'zh';
      applyLanguage();
    });
  }

  applyLanguage();
})();
