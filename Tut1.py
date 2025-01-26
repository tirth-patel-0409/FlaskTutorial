from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"


@app.route("/tirth")
def tirth():
    return "Hello Tirth Patel!"

# app.run()
app.run(debug=True)