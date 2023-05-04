from flask import Flask,request,render_template,redirect
from math import factorial
from fractions import Fraction
from fib import fib
from math import exp
app = Flask(__name__)



''' Reading Notes 
totalInput means the total number of input required. 
for example combonation needs 2 input to work properly.

'''
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



# fibonacci
@app.route("/fibonacci", methods=["GET","POST"])
def fibonacci():
    prob_data = {
        "type":"fibonacci",
        "totalInput" :1,
    }
    return render_template("solve.html", data=prob_data)



# simpleInterest
@app.route("/simpleinterest",methods=["GET","POST"])
def simpleinterest():
    prob_data = {
        "type":"simpleinterest",
        "totalInput" :3,
    }
    return render_template("solve.html",data=prob_data)
        
    


#CompoundInterest
@app.route("/compint", methods=["GET","POST"])
def compoundinterest():
    prob_data = {
        "type":"compoundinterest",
        "totalInput" :3,
    }
    
    return render_template("solve.html",data=prob_data)
    


#continuousinterest 
@app.route('/contint',methods=["GET","POST"])
def continuousinterest():
    prob_data = {
        "type":"continuousinterest",
        "totalInput" :3,
    }
    return render_template("solve.html",data=prob_data)
















'''
Below functions are the endpoints that calculate and return the answer to the solve.html
'''


# for combinations and permutations
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




# for arithmetic and geometric sequence
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



# for calculating fibonacci
@app.route('/fibcalc/<problemtype>',methods=["GET","POST"])
def fibcalc(problemtype):
    prob_data = {
        "type":"fibonacci",
        "totalInput" :1,
    }
    if problemtype=="fibonacci":
        if request.form["n"]:
            n = request.form['n']
            ans = fib(int(n))
            answer = { 
                "integer" : int(ans),
                "float":float(ans),
                "ratio": Fraction(ans)
                    }
            return render_template("solve.html",data=prob_data,answer=answer)
        else:
            return redirect(f"/{problemtype}")






@app.route("/intcalc/<problemtype>", methods=["POST"])
def intcalc(problemtype):
    prob_data = {
        "type":"simpleinterest",
        "totalInput" :3,
    }
    
    if problemtype=="simpleinterest":
        if request.form:
            p = request.form["p"]
            r= request.form["r"]
            t = request.form["t"]
            simpleinterest=(int(p) * float(r) * int(t))/100
            answer={
                "integer":int(simpleinterest),
                "float": float(simpleinterest)
            
              }
        
            return render_template("solve.html",data=prob_data,answer=answer)
        else:
            return redirect(f"/{problemtype}")
        
    
    prob_data = {
        "type":"compoundinterest",
        "totalInput" :4,
    }
    
    if problemtype=="compint":
        if request.form:
            p =  request.form["p"]
            r =request.form["r"]
            n=request.form["n"]
            t=request.form["t"]
            compoundinterest =int(p)*((1+ ((int(r)/100)/int(n)))**(int(n)*int(t)))
            answer={
                "integer":int(compoundinterest),
                "float": float(compoundinterest)
            
              }
            
            
            return render_template("solve.html",data=prob_data,answer=answer)
        else:
            return redirect("/intcalc/compint")
        
        
    prob_data = {
        "type":"continuousinterest",
        "totalInput" :3,
    }
    if problemtype=="contint":
        if request.form:
            p =  request.form["p"]
            r =float(request.form["r"])/100
            t=request.form["t"]
            
            continuousinterest = int(p)*exp(r*int(t))
            answer={
                "integer":int(continuousinterest),
                "float": "{:,.2f}".format(float(continuousinterest))
            
              }
            return render_template("solve.html",data=prob_data,answer=answer)
        else:
            return redirect("/intcalc/contint")
            
    
    
    
    
        
        
if __name__ == "__main__":
    app.run(debug=True)