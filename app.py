from flask import Flask,request,render_template,redirect
from math import factorial
from fractions import Fraction
app = Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html")


@app.route("/combination", methods=['GET','POST'])
def combination():
    # schema for a specific problem
    prob_data = {
        "type":"combination",
        "totalInput" : 2,
    }
    return render_template("solve.html", data=prob_data)


# this function will calculate and
@app.route("/calculate/<problemtype>", methods=["POST"])
def calculate(problemtype):
    prob_data = {
        "type":"combination",
        "totalInput" : 2,
    }
    if request.form['n'] and request.form['r']:
        if problemtype=="combination":
            n = int(request.form['n'])
            r = int(request.form['r'])
            # applying the formula of combinations which is 
            # n! / r!(n-r)!
            
            answer = { 
                    "integer" : int(factorial(n) / factorial(r) * factorial(abs(n-r))),
                    "float":float(factorial(n) / factorial(r) * factorial(abs(n-r))),
                    "ratio": Fraction(factorial(n) / factorial(r) * factorial(abs(n-r)))
                        }

            return render_template("solve.html",data=prob_data,answer=answer)
            
        else:
            return False
    else:
        return redirect('/combination')


if __name__ == "__main__":
    app.run(debug=True)