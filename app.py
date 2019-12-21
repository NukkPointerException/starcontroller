from flask import Flask, render_template
import subprocess
import os
import signal
import logging

# Flask server that allows invoker to remotely run python scripts that control the star

# Lets get some logging going
logger = logging.getLogger('StarController')
hdlr = logging.FileHandler('starcontroller.log')
formatter = logging.Formatter('%(asctime)s %(levelname)s %(message)s')
hdlr.setFormatter(formatter)
logger.addHandler(hdlr)
logger.setLevel(logging.INFO)

app = Flask(__name__)

# The PID of the currently running star controlling process
global_pid = -1


@app.route("/")
def main():
    # Main page with buttons
    return render_template('index.html')


@app.route("/on")
def turn_on():
    logger.info("Star mode: ON")
    global global_pid
    # stop previous process
    stop_process()
    # if it's hacky but it works, is it really hacky?
    process = subprocess.Popen(['python3', 'starcode/all_on.py'])
    # Record new PID so it can be stopped
    global_pid = process.pid
    return render_template('index.html')


@app.route("/off")
def turn_off():
    logger.info("Star mode: OFF")
    global global_pid
    stop_process()
    process = subprocess.Popen(['python3', 'starcode/all_off.py'])
    global_pid = process.pid
    return render_template('index.html')


@app.route("/twinkle")
def twinkle():
    logger.info("Star mode: TWINKLE")
    global global_pid
    stop_process()
    process = subprocess.Popen(['python3', 'starcode/twinkle.py'])
    global_pid = process.pid
    return render_template('index.html')


@app.route("/pulse")
def pulse():
    logger.info("Star mode: PULSE")
    global global_pid
    stop_process()
    process = subprocess.Popen(['python3', 'starcode/pulse.py'])
    global_pid = process.pid
    return render_template('index.html')


@app.route("/inout")
def inout():
    logger.info("Star mode: IN/OUT")
    global global_pid
    stop_process()
    process = subprocess.Popen(['python3', 'starcode/in_out.py'])
    global_pid = process.pid
    return render_template('index.html')


def stop_process():
    if global_pid != -1:
        os.kill(global_pid, signal.SIGTERM)


if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=False)
