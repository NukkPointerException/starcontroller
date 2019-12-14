from flask import Flask, render_template
app = Flask(__name__)


@app.route("/")
def main():
    return render_template('index.html')


@app.route("/on")
def turn_on():
    print("on")
    return render_template('index.html')


@app.route("/off")
def turn_off():
    print("off")
    return render_template('index.html')


@app.route("/twinkle")
def twinkle():
    print("twinkle")
    return render_template('index.html')


@app.route("/breathe")
def breathe():
    print("breathe")
    return render_template('index.html')


if __name__ == "__main__":
    app.run()
