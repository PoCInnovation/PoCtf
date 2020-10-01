#!/usr/bin/env node

const puppeteer = require("puppeteer");

closebrowser = browser => () => {
  if (browser && browser.close) {
    browser.close();
  }
};

async function visitPage(url, sleepTime) {
  const browser = await puppeteer.launch({
    args: ["--no-sandbox", "--disable-setuid-sandbox"]
  });

  const page = await browser.newPage();

  const cookies = [
    {
      url: url,
      httpOnly: true,
      name: "session",
      value: "eyJpZCI6MX0.XeD94w.3oC__mzIIRdsxn1WXyMdJh7HQlg"
    },
    {
      url: url,
      name: "flag",
      value: "PoC{XSS_M0R3_L!K3_FR33_C00K!35}"
    }
  ];

  await page.setCookie(...cookies);

  await page
    .goto(url, { waitUntil: "networkidle0" })
    .then((res) => res.text())
    .then(body => {console.log(body);})
    .catch((e) => {
      console.error(e);
    });

  setTimeout(closebrowser(browser), sleepTime);
}

sleepTime = 1000;

setInterval(() => {
  url = "http://front:3000/admin";
  visitPage(url, sleepTime);
}, sleepTime * 5);
