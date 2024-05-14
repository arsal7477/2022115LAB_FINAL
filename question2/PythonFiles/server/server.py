from flask import Flask

app = Flask(__name__)

@app.route('/')
def square_root():
    n = 25 
    return f"The square root of {n} is: {n ** 0.5}"

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)

