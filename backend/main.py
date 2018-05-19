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
    for customer in customers.json():
        print(customer["id"] == id)
        if customer["id"] == id:
            income = customer["householdIncome"]
    balance = getBankBalances(id)
    dict = {}
    dict["monthly_salary"] = income
    dict["savings"] = balance
    return jsonify(dict), 200

def getBankBalances(id):
    balance = 0
    accounts = requests.get(mock+"/bankAccounts")
    for account in accounts.json():
        if account["customerId"] == id:
            balance += account["balance"]
    return balance

if __name__ == "__main__":
    app.run(host='127.0.0.1', debug=True)
