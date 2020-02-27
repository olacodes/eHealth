
const ctx = document.getElementById('selfMedicationChart').getContext("2d")
fetch('http://localhost:8000/api/self-medication/')
.then(data => data.json()).then(data => {
    const labels = Object.keys(data).slice(1)
    const data = Object.values(data).slice(1)

    new Chart(ctx, {
        type: 'doughnut',
        data: {
            labels: labels,
            datasets: [{
                data: data,
                backgroundColor: ['red', 'green']
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