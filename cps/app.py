"""
This is the main file for the web app. It contains the Flask app and all the routes.
"""
import os
from services.system import system
from flask import Flask, render_template, request
app = Flask(__name__)

submissions = []

"""
This route is for the problem pages.
It takes the problem id as a parameter and renders the corresponding problem page.
"""
@app.route("/problem/<int:problem_id>")
def get_problem(problem_id: int) -> str:
    if problem_id == 1:
        return render_template("problem1.html")
    if problem_id == 2:
        return render_template("problem2.html")
    if problem_id == 3:
        return render_template("problem3.html")
    return render_template("404.html")

"""
This route is for the index page.
It renders the index page and handles the submission of code.
"""
@app.route("/", methods=["GET", "POST"])
def index() -> str:
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
            with open("cps/program_files/program.py", "w", encoding="utf8") as file:
                file.write(text)
        elif language == "C":
            file_extension = ".c"
            with open("cps/program_files/program.c", "w", encoding="utf8") as file:
                file.write(text)
        elif language == "C++":
            file_extension = ".cpp"
            with open("cps/program_files/program.cpp", "w", encoding="utf8") as file:
                file.write(text)
        elif language == "Java":
            file_extension = ".java"
            with open("cps/program_files/program.java", "w", encoding="utf8") as file:
                file.write(text)

        output, score = system(language, f"cps/program_files/program{file_extension}", problem)
        output = output.replace("\n", "<br>")
        submissions.append(output)

    submission_rows = "".join([f"<tr><td>{problem}</td><td>{submission}</td><td>{score}</td></tr>"
     for submission in submissions])
    return render_template("index.html", output=output, submission_rows=submission_rows)

if __name__ == "__main__":
    app.run()
