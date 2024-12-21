from flask import Flask,request,jsonify

app = Flask(__name__)

@app.route("/",methods = ["GET"])
def home():
    return ("<h1>hello</h1>")

@app.route("/checkvalue/<int:num>")
def Even_odd(num):
    if num%2 == 0:
        result = {
            "Num" :num,
            "Even" :True,
            "Server_IP": "192.168.1.1"
        }
    else:
        result = {
            "Num" :num,
            "Even" :False,
            "Server_IP": "192.168.1.1"
        }

    return jsonify(result)
    
if __name__ == "__main__":
    app.run(debug=True)