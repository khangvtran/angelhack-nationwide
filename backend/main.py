import requests
from flask import Flask, request, jsonify, render_template
from flask_cors import CORS



mock = "http://nw-angelhack-2018-mocks.us-east-1.elasticbeanstalk.com/"
onBoard = "https://search.onboard-apis.com/propertyapi/v1.0.0/"
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
	json = request.get_json() #type(data) = <dict>

	monthlyIncome = float(json["monthly_salary"])
	saving = float(json["savings"])
	percent = int(json["percent"])
	waitmonths = int(json["wait_months"])
	mortgageYears = int(json["mortgage_years"])

	monthlyPayment = monthlyIncome*percent/100
	downPayment = monthlyPayment*waitmonths + saving
	totalMortgagePayment = 12*mortgageYears*monthlyPayment

	totalPayment = downPayment + totalMortgagePayment
	d = {"price":totalPayment}

	return jsonify(d), 200

@app.route("/api/houseData", methods = ['POST'])
def getHouseData():
    import config
    json = request.get_json()
    postal = int(json["zipcode"])
    maxVal = float(json["price"])
    headers = {"apiKey" : config.key}
    payload = {"postalcode":postal, "minavmvalue":int(maxVal*0.95), "maxavmvalue":int(maxVal)}
    data = requests.get(onBoard+"property/snapshot", params=payload, headers = headers) # create an URL string
    return data.text, 200



if __name__ == "__main__":
    app.run(host='127.0.0.1', debug=True)
