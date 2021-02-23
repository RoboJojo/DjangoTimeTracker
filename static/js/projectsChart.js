window.onload = createChart();
function createChart(chartType = "pie") {
    let ctx = document.querySelector('#chart');
    let data = JSON.parse(ctx.dataset.data);
    let labels = JSON.parse(ctx.dataset.labels.replace(/'/g, '"'));
    let config = {
        type: chartType,
        data: {
            datasets: [{
                data: data,
                backgroundColor: getRandomColor(data.length)
            }],
            labels: labels
        },
        options: {
            tooltips: {
                callbacks: {
                    label: function (tooltipItem, data) {
                        let dataset = data.datasets[tooltipItem.datasetIndex];
                        let meta = dataset._meta[Object.keys(dataset._meta)[0]];
                        let total = meta.total;
                        let currentValue = dataset.data[tooltipItem.index];
                        let percentage = parseFloat((currentValue / total * 100).toFixed(1));
                        return secondsToDH(currentValue) + ' (' + percentage + '%)';
                    },
                    title: function (tooltipItem, data) {
                        return data.labels[tooltipItem[0].index];
                    }
                }
            },
        }
    };
    var char = new Chart(ctx, config);
};

function getRandomColor(amount) {
    let colors = [];
    for (let i = 0; i < amount; i++) {
        let letters = '0123456789ABCDEF';
        let color = '#';
        for (let i = 0; i < 6; i++) {
            color += letters[Math.floor(Math.random() * 16)];
        }
        colors.push(color);
    }
    return colors;
}

function secondsToDH(seconds) {
    seconds = Number(seconds);
    let d = (seconds / (3600*24)).toFixed(1);
    let h = (seconds % (3600*24) / 3600).toFixed(1);
    if (d < 1) {
        h = (seconds / 3600).toFixed(1);
        return h + "hrs";
    }
    return d + "days " + h + "hrs";
}