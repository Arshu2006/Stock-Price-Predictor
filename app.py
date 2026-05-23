from flask import Flask,render_template,request,jsonify
from model import predict_stock

app=Flask(__name__)

@app.route("/")
def home():

    return render_template("index.html")

@app.route("/predict",methods=["POST"])
def predict():

    stock=request.form["stock"]

    result=predict_stock(stock)

    return jsonify(
        {"prediction":result}
    )

if __name__=="__main__":

    app.run(debug=True)