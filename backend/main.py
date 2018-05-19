import requests
from flask import Flask, request, jsonify, render_template

mock = "http://nw-angelhack-2018-mocks.us-east-1.elasticbeanstalk.com/"
app = Flask(__name__,
    static_folder = "./../client/dist/static",
    template_folder = "./../client/dist")

@app.route("/")
def hello():
    return render_template("index.html")



@app.route("/api/customerBalances/<int:id>")
def getStuff(id):
    income = 0
    customers = requests.get(mock+"/customers")
    monthly_income = int([customer["householdIncome"] for customer in customers.json() if customer["id"] == id][0]/12)
    balance = getBankBalances(id)
    dict = {"monthly_salary":monthly_income, "savings":balance}
    return jsonify(dict), 200



def getBankBalances(id):
    balance = 0
    accounts = requests.get(mock+"/bankAccounts")
    balance = sum(account["balance"] for account in accounts.json() if account["customerId"] == id)
    return balance



if __name__ == "__main__":
    app.run(host='127.0.0.1', debug=True)
