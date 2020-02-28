var ctz = document.getElementById('smokeOrDrinkChart').getContext("2d")
        fetch('http://localhost:8100/api/health-habit/')
        .then(data => data.json()).then(data => {
           var labels = Object.keys(data)
           var data = Object.values(data)
           
           smoke_or_drink=data.slice(6, 9)
           label_smoke_or_drink=labels.slice(6,9)
           
            new Chart(ctz, {
                type: 'bar',

                data: {
                    labels: label_smoke_or_drink,
                    datasets: [{
                        label: 'Smoke or Drink',
                        data: smoke_or_drink,
                        backgroundColor: [
                            '#ffa600', '#ff6361', '#003f5c'
                        ],
                    },
                
                ]
                },
                options: {
                    scales:{
                        yAxes: [{
                            stacked: true,
                            ticks: {
                                beginAtZero: true
                            }
                        }],
                        xAxes: [{
                            stacked: true,
                            ticks: {
                                beginAtZero: true
                            }
                        }]
                    },
                    responsive: true,
                    legends: {
                        position: 'top'
                    }
                }
            })  
    })