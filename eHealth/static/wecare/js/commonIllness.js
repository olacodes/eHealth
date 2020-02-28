let cty = document.getElementById('commonIllnessChart').getContext("2d")

fetch('http://localhost:8100/api/common-illness/')
.then(data => data.json()).then(data => {
    var labels = Object.keys(data).slice(1)
    var data = Object.values(data).slice(1)

    new Chart(cty, {
        type: 'pie',
        data: {
            labels: labels,
            datasets: [{
                data: data,
                backgroundColor: [
                    '#003f5c', '#58508d', '#bc5090', '#ff6361', '#ffa600'
                ]
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