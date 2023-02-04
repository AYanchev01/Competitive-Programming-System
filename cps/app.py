from flask import Flask, render_template, request
from services.system import system
import os
app = Flask(__name__)

submissions = []

@app.route("/problem/<int:problem_id>")
def problem(problem_id):
    if problem_id == 1:
        return render_template("problem1.html")
    elif problem_id == 2:
        return render_template("problem2.html")
    elif problem_id == 3:
        return render_template("problem3.html")
    else:
        return render_template("404.html")

@app.route("/", methods=["GET", "POST"])
def index():
    language = ""
    problem = ""
    output = ""
    file_extension = ""
    if request.method == "POST":
        text = request.form["text"]
        problem = request.form["problem"]
        language = request.form["language"]
        os.mkdir("cps/program_files")
        if language == "Python":
            file_extension = ".py"
            with open("cps/program_files/program.py", "w") as f:
                f.write(text)
        elif language == "C":
            file_extension = ".c"
            with open("cps/program_files/program.c", "w") as f:
                f.write(text)
        elif language == "C++":
            file_extension = ".cpp"
            with open("cps/program_files/program.cpp", "w") as f:
                f.write(text)
        elif language == "Java":
            file_extension = ".java"
            with open("cps/program_files/program.java", "w") as f:
                f.write(text)

        output, score = system(language, f"cps/program_files/program{file_extension}", problem)
        output = output.replace("\n", "<br>")
        submissions.append(output)

    submission_rows = "".join([f"<tr><td>{problem}</td><td>{submission}</td><td>{score}</td></tr>" for submission in submissions])
    return render_template("index.html", output=output, submission_rows=submission_rows)

if __name__ == "__main__":
    app.run()
