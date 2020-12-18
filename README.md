# LONDON MOCK EXCHANGE API

The idea for this API was originated in a planning session amongst the four contributors listed on this repository. The decision was made to create this backend API so that others could use this as a template for their own trading app. This API works in conjunction with a static front end webpage built with React called London Mock Exchange. Check that out here: https://github.com/Oli-Le-Maire/london-mock-exchange-frontend.

We wanted to build a fun and interactive trading platform that beginners could use to see how different historical trades would have fared. This app is extendible from its current state to add more features should you desire. 

## Users:
The set up for this API is as follows. The User model is defined using the Django Rest Auth framework, however, we customized it to include a name. Should you wish to use the name category, you will need to add the name as one of the fields in the serializer. We use Rest-Auth's built in token authentication system.

## Portfolios:
The portfolio model is defined in the models section. It includes a name, a net earnings and an owner so that a particular user has ownership over the portfolio. The transaction model is also defined in portfolios as it is associated with the portfolio. The transaction can be inputted manually, but for our app, we used the marketstack api to gather data on trades. A transaction exists as a stock trade, with a buy and a sell date as the app is only compatible with historical trades currently.

For this API, we used Django and Django Rest Frameworks to build a backend that allows users to sign up, login, logout. 

## Set Up:

1. Clone this repo
2. Ensure you have python 3.9 downloaded on your system
3. Download pipenv from pythons package manager pip
4. In /london-mock-exchange-backend run `pipenv install` to install dependencies
5. run `pipenv shell` to activate your virtual environment
6. run `python manage.py migrate` to create your databases
7. run `python manage.py createsuperuser` to create a user that has access to the admin panel of Django
8. run `python manage.py runserver` to run the server and navigate to [localhost](http://localhost:8000) or if your console signifies another port, navigate to that instead of 8000

## Usage:

All routes begin with '/api/v1/'. You can create, read, update, and delete portfolios by sending the relevant request to 'api/v1/portfolio'. To create a transaction, send the request to 'api/v1/portfolio/{portfolio_id}/transaction