# save this as app.py
from flask import Flask, escape, request

app = Flask(__name__)

@app.route('/')
def hello():
    name = request.args.get("name", "This is capstone Project - by Prashant - V1")
    return f'Hello, {escape(name)}!'
		   
if __name__ == "__main__":
    # load pretrained model as clf
    app.run(host='0.0.0.0', port=80, debug=True) # specify port=80
