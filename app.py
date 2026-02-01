from flask import Flask, render_template, request, redirect, url_for
import json
import os

app = Flask(__name__)

DATA_FILE = "students.json"


def load_students():
    if not os.path.exists(DATA_FILE):
        return []
    with open(DATA_FILE, "r") as f:
        return json.load(f)


def save_students(students):
    with open(DATA_FILE, "w") as f:
        json.dump(students, f, indent=4)


# routes ->

@app.route("/")
def home():
    return render_template("index.html")


@app.route("/add", methods=["GET", "POST"])
def add_student():
    if request.method == "POST":
        students = load_students()

        student_id = len(students) + 1

        maths = int(request.form["maths"])
        science = int(request.form["science"])
        computer = int(request.form["computer"])

        total = maths + science + computer
        percent = (total / 300) * 100

        if percent >= 80:
            grade, remark = "A", "Excellent"
        elif percent >= 60:
            grade, remark = "B", "Good"
        else:
            grade, remark = "C", "Needs Improvement"

        student = {
            "id": student_id,
            "name": request.form["name"],
            "roll": request.form["roll"],
            "class": request.form["class"],
            "maths": maths,
            "science": science,
            "computer": computer,
            "total": total,
            "percentage": round(percent, 2),
            "grade": grade,
            "remark": remark
        }

        students.append(student)
        save_students(students)

        return redirect(url_for("view_report", student_id=student_id))

    return render_template("add_students.html")


#all students page ->

@app.route("/students")
def students_list():
    students = load_students()

    search_name = request.args.get("search")
    selected_class = request.args.get("class")

    # Unique class list
    classes = sorted(set(s["class"] for s in students))

    # 🔍 If teacher searched by NAME → ignore class
    if search_name:
        search_name = search_name.lower()
        students = [
            s for s in students
            if search_name in s["name"].lower()
        ]
        selected_class = None  # reset class

    # 🏫 Else if teacher selected CLASS → ignore search
    elif selected_class:
        students = [
            s for s in students
            if s["class"] == selected_class
        ]

    return render_template(
        "students.html",
        students=students,
        classes=classes,
        selected_class=selected_class,
        search_name=search_name
    )


# Individual report card page ->

@app.route("/report/<int:student_id>")
def view_report(student_id):
    students = load_students()
    student = next((s for s in students if s["id"] == student_id), None)
    return render_template("report.html", student=student)


if __name__ == "__main__":
    app.run(debug=True)
