function barChart(id, data, color) {
  const c = document.getElementById(id);
  const ctx = c.getContext("2d");
  c.width = c.offsetWidth;
  c.height = 200;

  const w = 40;
  const g = 20;

  data.forEach((v, i) => {
    ctx.fillStyle = color;
    ctx.fillRect(i * (w + g), c.height - v * 4, w, v * 4);
  });
}

function lineChart(id, data, color) {
  const c = document.getElementById(id);
  const ctx = c.getContext("2d");
  c.width = c.offsetWidth;
  c.height = 200;

  ctx.strokeStyle = color;
  ctx.beginPath();

  data.forEach((v, i) => {
    const x = i * 60;
    const y = c.height - v * 2;
    if (i === 0) ctx.moveTo(x, y);
    else ctx.lineTo(x, y);
  });

  ctx.stroke();
}

barChart("chart1", [10,20,30,40], "#ef4444");
lineChart("chart2", [65,59,80,81,56,55,40], "#22c55e");
barChart("chart3", [65,59,80,81,56,55,40], "#3b82f6");
barChart("chart4", [300,50,100], "#eab308");
