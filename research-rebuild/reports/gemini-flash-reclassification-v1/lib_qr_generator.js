const QRCode = require('/storage/Users/currentUser/Documents/岐伯论/research-rebuild/tools/node/node_modules/qrcode');

function cleanUrl(raw) {
  if (!raw) return '';
  let u = raw.trim().replace(/\)+$/, '');
  const mZhihu = u.match(/zhihu\.com\/question\/\d+\/answer\/(\d+)/);
  if (mZhihu) return 'https://zhihu.com/answer/' + mZhihu[1];
  u = u.replace('https://www.ifdian.net/', 'https://ifdian.net/');
  u = u.replace('https://www.zhihu.com/', 'https://zhihu.com/');
  return u;
}

async function generateQr(outPath, rawUrl) {
  const url = cleanUrl(rawUrl);
  return QRCode.toFile(outPath, url, {
    type: 'png',
    errorCorrectionLevel: 'L',
    width: 120,
    margin: 0,
    color: {
      dark: '#8F2D26',
      light: '#00000000'
    }
  });
}

module.exports = { cleanUrl, generateQr };
