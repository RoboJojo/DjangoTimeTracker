window.onload = function () {
    let ctx = document.querySelector('#chart');
    let data = JSON.parse(ctx.dataset.data);
    let labels = JSON.parse(ctx.dataset.labels.replace(/'/g, '"'));
    let config = {
        type: 'pie',
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
                        var dataset = data.datasets[tooltipItem.datasetIndex];
                        var meta = dataset._meta[Object.keys(dataset._meta)[0]];
                        var total = meta.total;
                        var currentValue = dataset.data[tooltipItem.index];
                        var percentage = parseFloat((currentValue / total * 100).toFixed(1));
                        return (currentValue / 60 / 60).toPrecision(2) + 'hrs (' + percentage + '%)';
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