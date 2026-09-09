(() => {
  const langStorageKey = 'site-lang';
  const themeStorageKey = 'site-theme';
  const langToggle = document.getElementById('langToggle');
  const themeToggle = document.getElementById('themeToggle');

  let lang = localStorage.getItem(langStorageKey) || 'zh';
  let theme = localStorage.getItem(themeStorageKey) || 'dark';

  function applyLanguage() {
    document.documentElement.lang = lang === 'zh' ? 'zh-CN' : 'en';
    document.querySelectorAll('.lang.zh').forEach((el) => { el.hidden = lang !== 'zh'; });
    document.querySelectorAll('.lang.en').forEach((el) => { el.hidden = lang !== 'en'; });
    if (langToggle) langToggle.textContent = lang === 'zh' ? 'English' : '中文';
    localStorage.setItem(langStorageKey, lang);
  }

  function applyTheme() {
    document.documentElement.dataset.theme = theme;
    document.documentElement.style.colorScheme = theme;
    if (themeToggle) {
      themeToggle.textContent = theme === 'dark' ? 'Light' : 'Dark';
      themeToggle.setAttribute('aria-pressed', theme === 'light' ? 'true' : 'false');
      themeToggle.setAttribute('title', theme === 'dark' ? 'Switch to light theme' : 'Switch to dark theme');
    }
    localStorage.setItem(themeStorageKey, theme);
  }

  if (langToggle) {
    langToggle.addEventListener('click', () => {
      lang = lang === 'zh' ? 'en' : 'zh';
      applyLanguage();
    });
  }

  if (themeToggle) {
    themeToggle.addEventListener('click', () => {
      theme = theme === 'dark' ? 'light' : 'dark';
      applyTheme();
    });
  }

  applyLanguage();
  applyTheme();
})();
