from flask import Flask, request, render_template
from calculator import add, subtract, multiply, divide

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    result = None
    if request.method == 'POST':
        num1 = float(request.form['num1'])
        num2 = float(request.form['num2'])
        operation = request.form['operation']
        
        if operation == 'add':
            result = add(num1, num2)
        elif operation == 'subtract':
            result = subtract(num1, num2)
        elif operation == 'multiply':
            result = multiply(num1, num2)
        elif operation == 'divide':
            try:
                result = divide(num1, num2)
            except ValueError as e:
                result = str(e)
    return render_template('index.html', result=result)


if __name__ == '__main__':
    app.run(debug=True)
