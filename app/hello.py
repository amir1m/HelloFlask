from flask import Flask,jsonify

app = Flask(__name__)

@app.route("/hello/<first_name>/<last_name>")
def hello(first_name, last_name):
    return jsonify({'msg':"Hello World", 'first_name':first_name, 'last_name':last_name})
    
if __name__ == "__main__":
    app.run()
