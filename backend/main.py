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
    customers = requests.get(mock+"/customers") #<class 'requests.models.Response'>, use .json() to convert to list
    monthly_income = int([customer["householdIncome"] for customer in customers.json() if customer["id"] == id][0]/12)
    balance = getBankBalances(id)
    dict = {"monthly_salary":monthly_income, "savings":balance}
    return jsonify(dict), 200


def getBankBalances(id):
    accounts = requests.get(mock+"/bankAccounts")
    balance = sum(account["balance"] for account in accounts.json() if account["customerId"] == id)
    return balance

@app.route("/api/processTotalFunds")
def getTotalFunds():
	data = request.data
	print(type(data))
	print(data)	



'''
{
	"monthly_salary": "200000",
	"savings": "1000000",
	"percent": "30",
	"waitmonths": "12"
}
'''

if __name__ == "__main__":
    app.run(host='127.0.0.1', debug=True)
