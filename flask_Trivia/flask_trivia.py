from flask import Flask
from flask import redirect
from flask import request
from flask import render_template

app = Flask(__name__)

@app.route("/")

html = """<style>
body {
  background-color: black;
  text-align: center;
  color: white;
  font-family: Arial, Helvetica, sans-serif;
}
</style>
</head>
<body>

<h1>TRIVIA TIME</h1>
<p>What is the meaning of life, the universe, and everything?</p>
<img src="https://stevetobak.com/wp-content/uploads/2021/02/dont-panic.png" alt="Avatar" style="width:200px">

    <form action = "/login" method = "POST">
        <p><input type = "text" name = "nm"></p>
        <p><input type = "submit" value = "submit"></p>
    </form>

</body>
</html>"""

def index():
    # Get a random trivia question
    response = requests.get("https://opentdb.com/api.php?amount=10")
    data = response.json()
    question = data["results"][0]["question"]
    # Render the HTML form
    return render_template("index.html", question=question)


@app.route("/", methods=["POST"])
def checkanswer():
    # Get the answer from the form
    answer = request.form.get("answer")
    # Get the correct answer from the API
    response = requests.get("https://opentdb.com/api.php?amount=1")
    data = response.json()
    correctanswer = data["results"][0]["correctanswer"]
    # Check if the answers match
    if answer == correctanswer:
        # Redirect the user to the "/correct" route
        return redirect("/correct")
    else:
        # Return them to the form to try again
        return redirect("/")


@app.route("/correct")
def correct():
    return "You got it right!"

@app.route("/")
def start():
    return html

@app.route("/login", methods = ["POST"])
def login():
        if request.form.get("nm") and request.form.get("nm") == "42":
                return redirect("/correct")
        else:
            return redirect("/")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=2224)
