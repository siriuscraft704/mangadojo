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

  function perspectiveEndpoint(start, end, vanishingPoint) {
    const x = start.x - vanishingPoint.x;
    const y = start.y - vanishingPoint.y;
    const lengthSquared = x * x + y * y;
    // Every direction is valid when the line starts at the vanishing point.
    if (lengthSquared < 1) return end;
    const t = ((end.x - start.x) * x + (end.y - start.y) * y) / lengthSquared;
    return {x: start.x + t * x, y: start.y + t * y};
  }

  function drawPerspectiveGuide(canvas, point, visible) {
    const context = canvas.getContext('2d');
    const {width, height} = canvas;
    context.clearRect(0, 0, width, height);
    if (!visible) return;
    context.save();
    context.lineWidth = 1.5;
    context.strokeStyle = '#aa456f75';
    context.beginPath();
    for (let i = 0; i <= 8; i++) {
      const x = width * i / 8;
      context.moveTo(point.x, point.y);
      context.lineTo(x, 0);
      context.moveTo(point.x, point.y);
      context.lineTo(x, height);
      if (i === 0 || i === 8) continue;
      const y = height * i / 8;
      context.moveTo(point.x, point.y);
      context.lineTo(0, y);
      context.moveTo(point.x, point.y);
      context.lineTo(width, y);
    }
    context.stroke();
    context.strokeStyle = '#873754';
    context.setLineDash([8, 6]);
    context.beginPath();
    context.moveTo(0, point.y);
    context.lineTo(width, point.y);
    context.stroke();
    context.setLineDash([]);
    context.fillStyle = '#873754';
    context.beginPath();
    context.arc(point.x, point.y, 5, 0, Math.PI * 2);
    context.fill();
    context.restore();
  }

  function reticleRadius(density, pitch) {
    return pitch * Math.sqrt(density / (100 * Math.PI));
  }

  function hasReticleArea(points) {
    if (points.length < 3) return false;
    const xs = points.map(point => point.x);
    const ys = points.map(point => point.y);
    return Math.max(...xs) - Math.min(...xs) >= 3 && Math.max(...ys) - Math.min(...ys) >= 3;
  }

  function fillReticle(canvas, points, {density, color, opacity, mirror}) {
    const pitch = 12;
    const tile = surface(pitch, pitch);
    const ink = tile.getContext('2d');
    ink.fillStyle = color;
    ink.beginPath();
    ink.arc(pitch / 2, pitch / 2, reticleRadius(density, pitch), 0, Math.PI * 2);
    ink.fill();

    const context = canvas.getContext('2d');
    const area = new Path2D();
    function addContour(contour) {
      area.moveTo(contour[0].x, contour[0].y);
      for (const point of contour.slice(1)) area.lineTo(point.x, point.y);
      area.closePath();
    }
    addContour(points);
    if (mirror) {
      // Reverse the reflected contour so overlapping areas keep the same winding.
      addContour(points.map(point => ({x: canvas.width - point.x, y: point.y})).reverse());
    }
    context.save();
    context.globalAlpha = opacity;
    context.fillStyle = context.createPattern(tile, 'repeat');
    context.fill(area);
    context.restore();
  }

  return {pressureWidth, surface, polygon, extract, transform, drawLayer,
    perspectiveEndpoint, drawPerspectiveGuide, reticleRadius, hasReticleArea, fillReticle};
})();
