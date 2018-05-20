# NaviGarden

## App Description

In [Nationwide Hackathon May 2018](http://nationwidehackathon.com/), five men came together to produce a wondrous creation of technology: NaviGarden. NaviGarden is a web application that assists millenial home buyers in navigating the complex chore of home buying, preparing them to be responsible home buyers. With a simple web browser, your typical millenial can input their financial data, visualize nearby homes they can afford, and make responsible decisions on purchasing their first home. 

## Design Elements 

# Front end

To install dependencies for Vue.js, write

`npm install`

from inside the *client* directory, and in the same directory, write

`npm run build`

in the terminal. This will allow the web application to be available for viewing in our server in `main.py`, which can be accessed via

`python main.py`

In the *backend* directory. 

## API's used:

+ We used [Vue.js](https://vuejs.org/) for implementing a front-end web application, which (George/Lorman add why we used this)

## How does it work?

Vue.js front-end with Google Material Design for UI/UX and Javascript as the programming language.

## Features

# Back end

+ [Flask](http://flask.pocoo.org/), a microframework that acts as our server to deploy the web application. Flask implements bare minimum requirements with simplicity, flexibility, and fine-grained control. 

+ [Flask CORS](http://flask-cors.readthedocs.io/en/latest/), which is a way to meet security settings to connect your back-end to your front-end.

+ [requests](http://docs.python-requests.org/en/master/) allows us to do HTTP requests to serve our backend to Flask.

+ [xmljson](https://pypi.org/project/xmljson/) parses XML files into JSON objects to parse response text from the Zillow API

## API's used:

+ [Nationwide API](https://app.swaggerhub.com/apis/NationwideInsurance/Hackathon-May-2018/1.0.0)

+ [Zillow API](https://www.zillow.com/howto/api/APIOverview.htm)

+ [Google Maps API](https://developers.google.com/maps/documentation/javascript/tutorial)

## How does it work?

We used Python to interact with REST APIs for the data

## Features

+ Flexibility in deployment using the Flask microframework

+ Produce stunning Google Maps API visualizations to see nearby homes that they can afford and have access to.

+ Access to metadata on available housing such as list price, number of bedrooms, and number of bathrooms.

# Other Components

+ Hosted on [AWS Elastic Beanstalk](https://aws.amazon.com/elasticbeanstalk/) for deployment of the web application.

+ Downloaded [Postman](https://www.getpostman.com/) to great a POST request from the results of our user input to the web application and send the zipcode, price, monthly salary, savings, and other financial information for back-end processing.


## What We Learned

+ Develop a web application that answers a specific business problem addressed by Nationwide's needs

+ Learn to solve a business problem influencing a demographic largely influencing Nationwide's company goals and needs.

+ Work with a team of people from various backgrounds, separate tasks via learning goals and expertise, and collaborate effectively via a version control system (Github) and in person




