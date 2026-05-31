const puppeteer = require("puppeteer");

(async () => {
  // DATA
  const url = process.argv[2];
  const selector = process.argv[3];

  // ABRIR NAVEGADOR
  const browser = await puppeteer.launch();

  // NUEVA PESTAÑA
  const page = await browser.newPage();

  // VIEWPORT
  await page.setViewport({ width: 1400, height: 1000, deviceScaleFactor: 1 });

  // URL
  await page.goto(url);
  await page.waitForSelector(selector);

  // ELEMENTO
  const element = await page.$(selector);

  // GUARDAR SCREENSHOT
  await element.screenshot({ path: "app/static/screenshots/cronograma.png" });

  await browser.close();
})();
