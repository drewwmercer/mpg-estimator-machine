from flask import Flask


app = Flask("mpg_estimator")

@app.route('/', methods=['GET'])
def ping():
    return "Pinging Model Application - Successful"

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=9696)
