let ctw = document.getElementById("exerciseRate").getContext("2d");
fetch("http://localhost:8100/api/health-habit/")
  .then(data => data.json())
  .then(data => {
    var labels = Object.keys(data);
    var data = Object.values(data);

    adequate_exercise = data.slice(0, 3);
    label_adequate_exercise = labels.slice(0, 3);

    new Chart(ctw, {
      type: "bar",

      data: {
        labels: label_adequate_exercise,
        datasets: [
          {
            label: "exercise",
            data: adequate_exercise,
            backgroundColor: ["#003f5c", "#58508d", "#bc5090"]
          }
        ]
      },
      options: {
        scales: {
          yAxes: [
            {
              stacked: true,
              ticks: {
                beginAtZero: true
              }
            }
          ],
          xAxes: [
            {
              stacked: true,
              ticks: {
                beginAtZero: true
              }
            }
          ]
        },
        responsive: true,
        legends: {
          position: "top"
        }
      }
    });
  });
