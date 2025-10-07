from flask import Flask, render_template, request
import math

app = Flask(__name__)

def sqrt(x):
    return math.sqrt(x)

def factorial(x):
    return math.factorial(x)

def ln(x):
    return math.log(x)

def power(x, b):
    return math.pow(x, b)

@app.route("/", methods=["GET", "POST"])
def index():
    result = None
    error = None
    if request.method == "POST":
        operation = request.form.get("operation")
        try:
            if operation == "sqrt":
                num = float(request.form.get("num"))
                result = f"√{num} = {sqrt(num)}"

            elif operation == "factorial":
                num = int(request.form.get("num"))
                result = f"{num}! = {factorial(num)}"

            elif operation == "ln":
                num = float(request.form.get("num"))
                result = f"ln({num}) = {ln(num)}"

            elif operation == "power":
                num = float(request.form.get("num"))
                base = float(request.form.get("base"))
                result = f"{num}^{base} = {power(num, base)}"

        except Exception as e:
            error = f"Error: {str(e)}"

    return render_template("index.html", result=result, error=error)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
