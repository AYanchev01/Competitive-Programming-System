from flask import Flask, render_template, request

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
    if request.method == "POST":
        text = request.form["text"]
        language = request.form["language"]
        submissions.append((text, language))
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
                <td>2 sec</td>
                <td>Easy</td>
            </tr>
            <tr>
                <td><a href="/problem/2">Sysadmin</a></td>
                <td>3 sec</td>
                <td>Medium</td>
            </tr>
            <tr>
                <td><a href="/problem/3">One more sequence</a></td>
                <td>3 sec</td>
                <td>Hard</td>
            </tr>
        </table>
        <div class="column">
            <form method="post">
                Text: <br>
                <textarea name="text" rows="10" cols="50"></textarea>
                <br>
                Language:
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
            Submitted text and language:<br>
            {'<br>'.join([f"{text} ({language})" for text, language in submissions])}
        </div>
    """

if __name__ == "__main__":
    app.run()
