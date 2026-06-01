function uploadFile() {
  const fileInput = document.getElementById("fileInput");
  const file = fileInput.files[0];
  const outputDiv = document.getElementById("output");
  const loader = document.getElementById("loader");

  if (!file) {
    alert("Please select a file first!");
    return;
  }

  const formData = new FormData();
  formData.append("file", file);

  loader.style.display = "block";
  outputDiv.innerHTML = "";

  fetch("http://127.0.0.1:5000/upload", {
    method: "POST",
    body: formData,
  })
    .then((response) => response.json())
    .then((data) => {
      loader.style.display = "none";
      outputDiv.innerHTML = `
            <p><strong>Time Taken:</strong> ${data.time_taken} seconds</p>
            <p><strong>Accuracy:</strong> ${data.accuracy}</p>
            ${formatReport(data.report)}
        `;
    })
    .catch((error) => {
      loader.style.display = "none";
      outputDiv.innerHTML = "Error: " + error;
    });
}

function formatReport(reportText) {
  const rows = reportText.trim().split("\n");
  let table = "<table><tr>";

  rows[0]
    .trim()
    .split(/\s+/)
    .forEach((col) => {
      table += `<th>${col}</th>`;
    });

  table += "</tr>";

  for (let i = 1; i < rows.length; i++) {
    table += "<tr>";
    rows[i]
      .trim()
      .split(/\s+/)
      .forEach((col) => {
        table += `<td>${col}</td>`;
      });
    table += "</tr>";
  }

  table += "</table>";
  return table;
}
