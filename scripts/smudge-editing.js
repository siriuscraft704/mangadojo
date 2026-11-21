/* Selection and mask operations for Smudge's raster layers. */
window.SmudgeEditing = (() => {
  function pressureWidth(event) {
    if (event.pointerType !== 'pen') return 1;
    return 0.25 + Math.max(0, Math.min(1, event.pressure)) * 0.75;
  }

  function surface(width, height) {
    const canvas = document.createElement('canvas');
    canvas.width = width;
    canvas.height = height;
    return canvas;
  }

  function polygon(context, points, offsetX = 0, offsetY = 0) {
    context.beginPath();
    points.forEach((point, index) => {
      if (index === 0) context.moveTo(point.x - offsetX, point.y - offsetY);
      else context.lineTo(point.x - offsetX, point.y - offsetY);
    });
    context.closePath();
  }

  function extract(canvas, points) {
    const xs = points.map(point => point.x);
    const ys = points.map(point => point.y);
    const left = Math.floor(Math.min(...xs));
    const top = Math.floor(Math.min(...ys));
    const width = Math.ceil(Math.max(...xs)) - left;
    const height = Math.ceil(Math.max(...ys)) - top;
    if (points.length < 3 || width < 3 || height < 3) return null;
    const pixels = surface(width, height);
    const context = pixels.getContext('2d');
    polygon(context, points, left, top);
    context.clip();
    context.drawImage(canvas, -left, -top);
    return {pixels, points, left, top, width, height};
  }

  function transform(canvas, selection, settings) {
    const context = canvas.getContext('2d');
    const {pixels, points, left, top, width, height} = selection;
    context.save();
    polygon(context, points);
    context.clip();
    context.clearRect(left, top, width, height);
    context.restore();
    context.save();
    context.translate(left + width / 2 + settings.x, top + height / 2 + settings.y);
    context.rotate(settings.angle * Math.PI / 180);
    context.scale(settings.scale, settings.scale);
    context.drawImage(pixels, -width / 2, -height / 2);
    context.restore();
  }

  function drawLayer(output, layer, buffer) {
    if (!layer.mask) {
      output.drawImage(layer.canvas, 0, 0);
      return;
    }
    const context = buffer.getContext('2d');
    context.clearRect(0, 0, buffer.width, buffer.height);
    context.drawImage(layer.canvas, 0, 0);
    context.globalCompositeOperation = 'destination-out';
    context.drawImage(layer.mask, 0, 0);
    context.globalCompositeOperation = 'source-over';
    output.drawImage(buffer, 0, 0);
  }

  return {pressureWidth, surface, polygon, extract, transform, drawLayer};
})();
