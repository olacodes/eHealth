
var ctx = document.getElementById('commonIllness-chart').getContext("2d")

fetch('http://localhost:8000/api/common-illness/')
.then(data => data.json()).then(data => {
    var labels = Object.keys(data).slice(1)
    var data = Object.values(data).slice(1)

    new Chart(ctx, {
        type: 'pie',
        data: {
            labels: labels,
            datasets: [{
                data: data,
                backgroundColor: ['blue', 'red', 'green']
            }]
        },
        options: {
            responsive: true,
            legends: {
                position: 'top'
            }
        }
    })
})


