window.ProjectChart = null;
window.onload = createChart();
function createChart(chartType = "pie") {
    if(window.ProjectChart !== null){
        window.ProjectChart.destroy();
    }
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
    window.ProjectChart = new Chart(ctx, config);
};

function getRandomColor(amount) {
    let colors = [];
    for (let i = 0; i < amount; i++) {
        let color = '#'+Math.floor(Math.random()*16777215).toString(16);
        if (colors.find(element => element === color) === undefined) {
            colors.push(color);
        }
        else {
            i--;
        }
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