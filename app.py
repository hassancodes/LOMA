from flask import Flask
from flask import render_template
app = Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html")


@app.route("/combinations")
def combinations():
    # schema for a specific problem
    prob_data = {
        "type":"combination",
        "totalInput" : 2,
    }
    return render_template("solve.html", data=prob_data)


# this function will calculate and
@app.route("/calculate/<problemtype>", methods=["POST"])
def calculate():
    pass

if __name__ == "__main__":
    app.run(debug=True)