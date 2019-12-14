from flask import Flask, render_template
import subprocess
import os
import signal

app = Flask(__name__)

# Server that allows invoker to remotely call code that controls the star

# The PID of the currently running star controlling process
global_pid = -1


@app.route("/")
def main():
    # Main page with buttons
    return render_template('index.html')


@app.route("/on")
def turn_on():
    global global_pid
    print("on")
    # stop previous process
    stop_process()
    # if it's hacky but it works, is it really hacky?
    process = subprocess.Popen(['python3', 'starcode/all_on.py'])
    # Record new PID so it can be stopped
    global_pid = process.pid
    print("Current PID: ")
    print(global_pid)
    return render_template('index.html')


@app.route("/off")
def turn_off():
    global global_pid
    print("off")
    # stop previous process
    stop_process()
    # if it's hacky but it works, is it really hacky?
    process = subprocess.Popen(['python3', 'starcode/all_off.py'])
    # Record new PID so it can be stopped
    global_pid = process.pid
    print("Current PID: ")
    print(global_pid)
    return render_template('index.html')


@app.route("/twinkle")
def twinkle():
    print("twinkle")
    return render_template('index.html')


@app.route("/breathe")
def breathe():
    print("breathe")
    return render_template('index.html')


def stop_process():
    if global_pid != -1:
        os.kill(global_pid, signal.SIGTERM)


if __name__ == "__main__":
    app.run()
