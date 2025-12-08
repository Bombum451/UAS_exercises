from flask import Flask, request

app = Flask(__name__)
@app.route('/prime_number/<number>')
def echo(number):
    n = int(number)
    divisors = 0

    for x in range(1, n + 1):
        if n % x == 0:
            divisors = divisors + 1
            #print("divisible by " + str(x))

    if divisors == 2:
        return '{"Number":' + str(n) + ', "isPrime":true}'
    else:
        return '{"Number":' + str(n) + ', "isPrime":false}'

if __name__ == '__main__':
    app.run(use_reloader=True, host='127.0.0.1', port=5000)