from flask import Flask, render_template, flash, redirect, request, session, logging, url_for,jsonify


app = Flask(__name__)



@app.route('/')
def home():

    return jsonify({"message":"home"})

if __name__ == '__main__':
    
        
    app.run(debug=True)
