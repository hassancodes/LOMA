from flask import Flask,request,render_template,redirect
from math import factorial
from fractions import Fraction
app = Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html")

# routing to problem page starts from here
@app.route("/combination", methods=['GET','POST'])
def combination():
    # schema for a specific problem
    prob_data = {
        "type":"combination",
        "totalInput" : 2,
    }
    return render_template("solve.html", data=prob_data)



# permutation
@app.route("/permutation", methods=["GET","POST"])
def permuation():
    prob_data = {
        "type":"permutation",
        "totalInput" : 2,
    }
    return render_template("solve.html", data=prob_data)



# arithmeticsequence
@app.route("/arithmeticsequence", methods=["GET","POST"])
def arithmeticsequence():
    prob_data = {
        "type":"arithmeticsequence",
        "totalInput" : 3,
    }
    return render_template("solve.html", data=prob_data)
    

# geometricsequence
@app.route("/geometricsequence", methods=["GET","POST"])
def geometricsequence():
    prob_data = {
        "type":"geometricsequence",
        "totalInput" : 3,
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
        # combination starts from here
        if problemtype=="combination":
            n = int(request.form['n'])
            r = int(request.form['r'])
            # applying the formula of combinations which is 
            # n! / r!(n-r)!
            ans = factorial(n) / (factorial(r) * factorial(abs(n-r)))
            answer = { 
                    "integer" : int(ans),
                    "float":float(ans),
                    "ratio": Fraction(ans)
                        }

            return render_template("solve.html",data=prob_data,answer=answer)
        
        # #####------permuation------########## starts from here
        if problemtype=="permutation":
            n = int(request.form['n'])
            r = int(request.form['r'])
            # applying the formula of permutation which is 
            # n! /(n-r)!
            #lets goo
            ans = factorial(n) /factorial(abs(n-r))
            answer = { 
                    "integer" : int(ans),
                    "float":float(ans),
                    "ratio": Fraction(ans)
                        }

            return render_template("solve.html",data=prob_data,answer=answer)
                
        # #####------permuation------########## ends here
               
        
        
        
        else:
            return False
    else:
        return redirect(f"/{problemtype}")




@app.route("/calcseq/<problemtype>",methods=["POST"])
def calcseq(problemtype):
    arithmeticsequence = {
        "type":"arithmeticsequence",
        "totalInput" : 3,
        
    }
    geometricsequence = {
        "type":"geometricsequence",
        "totalInput" : 3,
        
    }
        # #####------arithmeticsequence------########## starts here
    if problemtype=="arithmeticsequence":
        a1 = int(request.form['a1'])
        an = int(request.form['an'])
        d = int(request.form['d'])
        # applying the formula of permutation which is 
        # n! /(n-r)!
        ans = a1 + ((an-1) * d)
        answer = { 
                "integer" : int(ans),
                "float":float(ans),
                "ratio": Fraction(ans)
                    }

        return render_template("solve.html",data=arithmeticsequence,answer=answer)
    
    
    if problemtype=="geometricsequence":
        a1 = int(request.form['a1'])
        n = int(request.form['n'])
        r = int(request.form['r'])
    # geometric sequence formula, this will search the nth term in the sequence
        ans = a1 * (r**(n-1))
        answer = { 
                "integer" : int(ans),
                "float":float(ans),
                "ratio": Fraction(ans)
                    }

        return render_template("solve.html",data=geometricsequence,answer=answer)
  
    
    else:
        return redirect(f"/{arithmeticsequence}")



if __name__ == "__main__":
    app.run(debug=True)