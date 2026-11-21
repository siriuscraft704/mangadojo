/* Render the comic as a printable PNG while keeping reference proportions. */
window.MangaDojoComic = (() => {
  function imageFrom(url) {
    const image = new Image();
    image.src = url;
    return image.decode().then(() => image);
  }

  function contain(context, image, x, y, width, height) {
    const scale = Math.min(width / image.naturalWidth, height / image.naturalHeight);
    const w = image.naturalWidth * scale, h = image.naturalHeight * scale;
    context.drawImage(image, x + (width - w) / 2, y + (height - h) / 2, w, h);
  }

  async function readImage(file) {
    if (!['image/png','image/jpeg','image/webp'].includes(file.type) || file.size > 12 * 1024 * 1024) {
      throw new Error('Use uma imagem PNG, JPEG ou WebP de até 12 MB.');
    }
    const url = URL.createObjectURL(file);
    try {
      const image = await imageFrom(url);
      const scale = Math.min(1, 900 / Math.max(image.naturalWidth, image.naturalHeight));
      const canvas = document.createElement('canvas');
      canvas.width = Math.max(1, Math.round(image.naturalWidth * scale));
      canvas.height = Math.max(1, Math.round(image.naturalHeight * scale));
      const context = canvas.getContext('2d');
      context.fillStyle = 'white';
      context.fillRect(0, 0, canvas.width, canvas.height);
      contain(context, image, 0, 0, canvas.width, canvas.height);
      return canvas.toDataURL('image/webp', 0.78);
    } finally {
      URL.revokeObjectURL(url);
    }
  }

  function writeLines(context, value, x, y, width, maxLines) {
    const lines = [];
    let current = '';
    for (const word of value.trim().split(/\s+/)) {
      for (const part of word.match(/.{1,29}/gu) || []) {
        const next = current ? current + ' ' + part : part;
        if (current && context.measureText(next).width > width) {
          lines.push(current);
          current = part;
        } else current = next;
      }
    }
    if (current) lines.push(current);
    const visible = lines.slice(0, maxLines);
    if (lines.length > maxLines) visible[maxLines - 1] += '…';
    visible.forEach((line,index) => context.fillText(line,x,y + index * 25,width));
  }

  async function render(canvas, panels, fields) {
    const columns = Number(fields.columns) === 1 ? 1 : 2;
    const reversed = fields.direction === 'Da direita para a esquerda';
    const images = await Promise.all(panels.map(panel => panel.image ? imageFrom(panel.image).catch(() => null) : null));
    const rows = Math.ceil(panels.length / columns);
    const margin = 32, gap = 18, heading = 90, rowHeight = 390;
    const width = (1000 - margin * 2 - gap * (columns - 1)) / columns;
    canvas.width = 1000;
    canvas.height = heading + rows * (rowHeight + gap) + margin - gap;
    const context = canvas.getContext('2d');
    context.fillStyle = '#fff';
    context.fillRect(0, 0, canvas.width, canvas.height);
    context.fillStyle = '#282633';
    context.font = 'bold 36px Georgia';
    context.fillText(fields.title?.trim() || 'Página de mangá',margin,57,canvas.width - 2 * margin);
    panels.forEach((panel,index) => {
      const column = index % columns;
      const x = margin + (reversed ? columns-1-column : column)*(width+gap);
      const y = heading + Math.floor(index / columns)*(rowHeight+gap);
      context.strokeStyle = '#282633';
      context.lineWidth = 3;
      context.strokeRect(x,y,width,rowHeight);
      if(images[index]) contain(context,images[index],x+8,y+8,width-16,272);
      else {
        context.fillStyle = '#f3edf0';
        context.fillRect(x+8,y+8,width-16,272);
        context.fillStyle = '#615260';
        context.font = '20px system-ui';
        writeLines(context,panel.shot || 'Quadro '+(index+1),x+24,y+130,width-48,4);
      }
      if(panel.dialogue){
        context.fillStyle = '#282633';
        context.font = '21px system-ui';
        writeLines(context,panel.dialogue,x+16,y+303,width-32,4);
      }
    });
  }

  return {readImage,render};
})();
