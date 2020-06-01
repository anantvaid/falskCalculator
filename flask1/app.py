from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

@app.route('/',methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/math',methods=['POST'])
def math_operation():
    if (request.method == 'POST'):
        operation = request.form['operation']
        num1 = int(request.form['num1'])
        num2 = int(request.form['num2'])
        if (operation == 'add'):
            result = 'the sum of {} and {} is {}'.format(num1, num2, num1 + num2)
        if (operation == 'sub'):
            result = 'the difference of {} and {} is {}'.format(num1, num2, num1 - num2)
        if (operation == 'mul'):
            result = 'the product of {} and {} is {}'.format(num1, num2, num1 * num2)
        if (operation == 'div'):
            result = 'the quotient of {} and {} is {}'.format(num1, num2, num1 // num2)
        return render_template('results.html', result=result)

@app.route('/via_postman',methods=['POST'])   #For calling the web API
def math_operation_via_postman():
    if (request.method == 'POST'):
        operation=request.json['operation']
        num1=int(request.json['num1'])
        num2=int(request.json['num2'])
        if (operation == 'add'):
            result = 'the sum of {} and {} is {}'.format(num1,num2,num1+num2)
        if (operation == 'sub'):
            result = 'the difference of {} and {} is {}'.format(num1, num2, num1 - num2)
        if (operation == 'mul'):
            result = 'the product of {} and {} is {}'.format(num1, num2, num1 * num2)
        if (operation == 'div'):
            result = 'the quotient of {} and {} is {}'.format(num1, num2, num1 // num2)
        return jsonify(result)

if __name__ == '__main__':
    print('The app is working')
    app.run()