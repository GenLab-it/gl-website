from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def comingsoon():
    return render_template('comingsoon.html')


if __name__ == '__main__':
    app.run(debug=True)