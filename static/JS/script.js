document.addEventListener("DOMContentLoaded", () => {

  const form = document.getElementById("studentForm");

  if (form) {
    form.addEventListener("submit", function (e) {
      e.preventDefault();

      const student = {
        name: document.getElementById("name").value,
        roll: document.getElementById("roll").value,
        className: document.getElementById("class").value,
        maths: parseInt(document.getElementById("maths").value),
        science: parseInt(document.getElementById("science").value),
        computer: parseInt(document.getElementById("computer").value)
      };

      localStorage.setItem("studentData", JSON.stringify(student));
      window.location.href = "/report";
    });
  }

  const data = localStorage.getItem("studentData");

  if (data && document.getElementById("rName")) {
    const s = JSON.parse(data);
    const total = s.maths + s.science + s.computer;
    const percent = ((total / 300) * 100).toFixed(2);

    let grade = "C";
    let remark = "Needs Improvement";

    if (percent >= 80) {
      grade = "A";
      remark = "Excellent";
    } else if (percent >= 60) {
      grade = "B";
      remark = "Good";
    }

    document.getElementById("rName").innerText = s.name;
    document.getElementById("rRoll").innerText = s.roll;
    document.getElementById("rClass").innerText = s.className;
    document.getElementById("rMaths").innerText = s.maths;
    document.getElementById("rScience").innerText = s.science;
    document.getElementById("rComputer").innerText = s.computer;
    document.getElementById("rTotal").innerText = total;
    document.getElementById("rPercent").innerText = percent;
    document.getElementById("rGrade").innerText = grade;
    document.getElementById("rRemark").innerText = remark;
  }
});
