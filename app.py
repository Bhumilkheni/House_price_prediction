import pickle

from flask import Flask, render_template, request

app = Flask(__name__)
model = pickle.load(open("Models/House_prediction.pkl", "rb"))


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/prediction", methods=["GET", "POST"])
def predict_data():
    if request.method == "POST":
        CRIM = float(request.form.get("CRIM"))
        ZN = float(request.form.get("ZN"))
        INDUS = float(request.form.get("INDUS"))
        CHAS = int(request.form.get("CHAS"))
        NOX = float(request.form.get("NOX"))
        RM = float(request.form.get("RM"))
        AGE = float(request.form.get("AGE"))
        DIS = float(request.form.get("DIS"))
        RAD = int(request.form.get("RAD"))
        TAX = int(request.form.get("TAX"))
        PTRATIO = float(request.form.get("PTRATIO"))
        B = float(request.form.get("B"))
        LSTAT = float(request.form.get("LSTAT"))

        data = [[CRIM, ZN, INDUS, CHAS, NOX, RM, AGE, DIS, RAD, TAX, PTRATIO, B, LSTAT]]
        result = model.predict(data)
        return render_template("home.html", result=result[0])
    else:
        return render_template("home.html")


if __name__ == "__main__":
    app.run(host="0.0.0.0")
