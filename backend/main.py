import requests
import json
from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
from xmljson import parker as xmlparse, Parker
from xml.etree.ElementTree import fromstring
import config


mock = "http://nw-angelhack-2018-mocks.us-east-1.elasticbeanstalk.com/"
onBoard = "https://search.onboard-apis.com/propertyapi/v1.0.0/"
zillow = "http://www.zillow.com/webservice/"
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
    rjson = request.get_json()
    postal = int(rjson["zipcode"])
    maxVal = float(rjson["price"])
    headers = {"accept":"application/json", "apiKey" : config.onboard_key}
    payload = {"postalcode":postal, "minavmvalue":int(maxVal*0), "maxavmvalue":int(maxVal), "pagesize":20}
    data = requests.get(onBoard+"property/snapshot", params=payload, headers = headers)
    if data.status_code != 200:
        return 503
    return data.text, 200

# https://www.zillow.com/howto/api/GetDeepSearchResults.htm
@app.route("/api/callZillowApi", methods = ['POST'])
def callZillowApi():
    address = request.get_json()
    #zillow call
    payload = {"zws-id":config.zillow_key, "address":address["line1"], "citystatezip":address["locality"]+","+address["countrySubd"]}
    resp = requests.get(zillow+"GetDeepSearchResults.htm", params=payload)
    json_data = json.loads(json.dumps(xmlparse.data(fromstring(resp.text))))
    if json_data["message"]["code"] != 0:
        return 503
    #also google maps
    print(json.dumps(json_data["response"]["results"]["result"]))
    payload = {"location":address["oneLine"], "size":"600x400", "key":config.google_api_key}
    resp = requests.get("https://maps.googleapis.com/maps/api/streetview", params=payload)
    print(resp.text)
    return json.dumps(json_data["response"]["results"]), 200


if __name__ == "__main__":
    app.run(host='127.0.0.1', debug=True)
