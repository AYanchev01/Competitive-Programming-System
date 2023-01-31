from flask import Flask, render_template, request
from system import system
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
    file_extension = ""
    output = ""
    if request.method == "POST":
        text = request.form["text"]
        problem = request.form["problem"]
        language = request.form["language"]
        submissions.append((text, problem, language))
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

        output = system(language, f"cps/program_files/program{file_extension}", problem)
        output = output.replace("\n", "<br>")
    return f"""
        <style>
            h1 {{
                text-align: center;
            }}
            table {{
                width: 100%;
            }}
            td, th {{
                border: 1px solid black;
                padding: 8px;
                text-align: left;
            }}
            .column {{
                float: left;
                width: 50%;
                padding: 10px;
            }}
        </style>
        <h1>Competitive programming system</h1>
        <table>
            <tr>
                <th>Problem</th>
                <th>Time Limit</th>
                <th>Difficulty</th>
            </tr>
            <tr>
                <td><a href="/problem/1">Palindrome</a></td>
                <td>0.5 sec</td>
                <td>Easy</td>
            </tr>
            <tr>
                <td><a href="/problem/2">Sysadmin</a></td>
                <td>0.2 sec</td>
                <td>Medium</td>
            </tr>
            <tr>
                <td><a href="/problem/3">One more sequence</a></td>
                <td>0.3 sec</td>
                <td>Hard</td>
            </tr>
        </table>
        <div class="column">
            <form method="post">
                Source code: <br>
                <textarea name="text" rows="20" cols="140"></textarea>
                <br>
                <select name="problem">
                    <option value="Palindrome">Palindrome</option>
                    <option value="Sysadmin">Sysadmin</option>
                    <option value="One more sequence">One more sequence</option>
                </select>
                <select name="language">
                    <option value="Python">Python</option>
                    <option value="C">C</option>
                    <option value="C++">C++</option>
                    <option value="Java">Java</option>
                </select>
                <input type="submit" value="Submit">
            </form>
        </div>
        <div class="column">
            Submitions:<br>
            {output}
        </div>
    """

if __name__ == "__main__":
    app.run()
