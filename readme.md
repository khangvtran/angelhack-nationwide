# HouseFinder

## App Description

At [AngelHack Nationwide](http://nationwidehackathon.com/), five men came together to produce a wondrous creation of technology: HouseFinder. A web application that aims to assist millenials in navigating the complex chore of choosing a long-term housing solution and prepare them to be responsible property buyers. With a simplistic and interactive UI, one is presented with data which corresponds to their current financial situation.

![MapPin](https://farm2.staticflickr.com/1727/41842743535_0158456be6_h.jpg = 24x48)



## Design Elements 

## Build Instructions
```
$ git clone ??
$ cd angelhack-nationwide
$ pip install -r requirements.txt
$ cd client
$ npm run build
```

# Front End
We used [Vue.js](https://vuejs.org/) as the main framework and utilized Google's [Material Design](https://material.io/) elements for simplistic and elegant UI design.

## How does it work?
1. A user can either be a Nationwide customer or a non-Nationwide customer. By being a Nationwide customer, financial data is aggregrated from the database to estimate how much money they can afford to commit towards a property. 
2. User is prompted to enter monthly salary and how long they wish to have a mortgage loan, if applicable.
3. Up to 10 properties which fall within a most probable range are pin-pointed on a map within in a zip-code area of choice.

### Features
+ Produce stunning Google Maps API visualizations to see nearby homes that they can afford and have access to.
+ Dynamic web pages‽ What are page reloads for anyway?

# Back end
Queries APIs and returns necessary data to serve

## Frameworks
+ [Flask](http://flask.pocoo.org/), a microframework that acts as our server to deploy the web application. Flask implements bare minimum requirements with simplicity, flexibility, and fine-grained control. 
+ [Flask CORS](http://flask-cors.readthedocs.io/en/latest/), which is a way to meet security settings to connect your back-end to your front-end.
+ [requests](http://docs.python-requests.org/en/master/), HTTP requests for API calls
+ [xmljson](https://pypi.org/project/xmljson/), parses XML returned from Zillow API into JSON

## API's used:
+ [Nationwide API](https://app.swaggerhub.com/apis/NationwideInsurance/Hackathon-May-2018/1.0.0)
+ [Zillow API](https://www.zillow.com/howto/api/APIOverview.htm)
+ [Google Maps API](https://developers.google.com/maps/documentation/javascript/tutorial)


## Features
+ Flexibility in deployment using the Flask microframework
+ Access to metadata on available housing such as list price, number of bedrooms, and number of bathrooms.

# Other Components
+ Backend hosted on **[AWS EC2](https://aws.amazon.com/elasticbeanstalk/)** for scalability
+ **[Postman](https://www.getpostman.com/)** - cURL requests made easy to assert the test results of our user input to the web application.
###### cURL > Postman jk


## What We Learned
+ Develop a web application that caters toward a specific business problem addressed by Nationwide's
+ Learn to solve a business problem influencing a demographic largely influencing Nationwide's company goals and needs.
+ Work with a team of people from various backgrounds, separate tasks via learning goals and expertise, and collaborate effectively via a version control system (Github) and in person
+ Our platform relies on using API calls to the Nationwide and Zillow APIs to query the data when needed (as JSON objects). 



