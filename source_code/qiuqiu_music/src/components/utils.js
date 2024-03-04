export default function imageToDataUrl(imagePath) {
  return new Promise(function(resolve, reject) {
    var img = new Image();
    img.onload = function() {
      var canvas = document.createElement('canvas');
      canvas.width = img.width;
      canvas.height = img.height;

      var ctx = canvas.getContext('2d');
      ctx.drawImage(img, 0, 0);

      var dataUrl = canvas.toDataURL('image/png');
      resolve(dataUrl);
    };

    img.onerror = function() {
      reject(new Error('Failed to load image: ' + imagePath));
    };

    img.src = imagePath;
  });
}
