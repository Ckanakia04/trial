from flask import Flask, redirect, url_for, render_template, request
import sys

userSelection = {
    "second":"",
    "third":""
}

app = Flask(__name__)

@app.route('/')
def hello():
    userSelection.update({
        "second":"",
        "third":""
    })
    return render_template("child1.html",userSelection=userSelection)

@app.route('/child2')
def child2():
    data = request.args.get('data')
    userSelection["second"] = data
    return render_template("child2.html",data=data,userSelection=userSelection)

@app.route('/child3')
def child3():
    data = request.args.get('finalData')
    userSelection["third"] = data
    trial = "haha"
    return render_template("child3.html",finalData=userSelection)
    


if __name__ == '__main__':
    app.run(debug=True)