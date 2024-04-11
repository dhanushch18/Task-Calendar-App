from flask import Flask, render_template

app=Flask(__name__)

@app.route("/")
def hi():
    return render_template('t1.html')