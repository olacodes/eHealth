const ctx = document.getElementById("selfMedicationChart").getContext("2d");
fetch("http://localhost:8100/api/self-medication/")
  .then(data => data.json())
  .then(data => {
    const labels = Object.keys(data).slice(1);
    const datas = Object.values(data).slice(1);

    new Chart(ctx, {
      type: "doughnut",
      data: {
        labels: labels,
        datasets: [
          {
            label: "Self Medication Chart Analysis",
            data: datas,
            backgroundColor: ["#bc5090", "#58508d"]
          }
        ]
      },
      options: {
        responsive: true,
        legends: {
          position: "top"
        }
      }
    });
  });
