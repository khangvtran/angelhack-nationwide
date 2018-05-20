import requests
from flask import Flask, request, jsonify, render_template
from flask_cors import CORS



mock = "http://nw-angelhack-2018-mocks.us-east-1.elasticbeanstalk.com/"
app = Flask(__name__,
    static_folder = "./../client/dist/static",
    template_folder = "./../client/dist")
CORS(app)

@app.route("/")
def hello():
    return render_template("index.html")

# get data from GET
@app.route("/api/customerBalances", methods = ['GET']) #example url = localhost:port/api/customerBalances?id=
def getStuff():
    id = int(request.args.get("id"))
    customers = requests.get(mock+"/customers") #<class 'requests.models.Response'>, use .json() to convert to list of dict
    monthly_income = int([customer["householdIncome"] for customer in customers.json() if customer["id"] == id][0]/12)
    balance = getBankBalances(id)
    d = {"monthly_salary":monthly_income, "savings":balance}
    return jsonify(d), 200


def getBankBalances(id):
    accounts = requests.get(mock+"/bankAccounts")
    balance = sum(account["balance"] for account in accounts.json() if account["customerId"] == id)
    return balance


# get data from POST
@app.route("/api/processTotalFunds", methods = ['POST'])
def getTotalFunds():
	data = request.get_json() #type(data) = <dict> 

	monthlyIncome = float(data["monthly_salary"])
	saving = float(data["savings"])
	percent = int(data["percent"])
	waitmonths = int(data["wait_months"])
	mortgageYears = int(data["mortgage_years"])

	monthlyPayment = monthlyIncome*percent/100
	downPayment = monthlyPayment*waitmonths + saving
	totalMortgagePayment = 12*mortgageYears*monthlyPayment

	totalPayment = downPayment + totalMortgagePayment
	d = {"price":totalPayment}

	return jsonify(d), 200





'''

>>> import ast
>>> ast.literal_eval("{'muffin' : 'lolz', 'foo' : 'kitty'}")
{'muffin': 'lolz', 'foo': 'kitty'}



{
	"monthly_salary": "200000",
	"savings": "1000000",
	"percent": "30",
	"wait_months": "12"
	"mortgage_years": "40"
	""
}
'''

if __name__ == "__main__":
    app.run(host='127.0.0.1', debug=True)
