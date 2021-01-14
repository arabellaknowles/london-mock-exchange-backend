# London Mock Exchange API
This is a backend API created for trading applications, managing users, portfolio and transactions. For a compatible static frontend user interface, checkout this [London Mock Exchange repository](https://github.com/arabellaknowles/london-mock-exchange-frontend). Click [here](http://londonmockexchange.surge.sh/) to view the live website. 

## Usage:
Our API is deployed on heroku : https://london-mock-exchange.herokuapp.com/api/v1   
An authentication token is required for any portfolio route requests.

| URL | HTTP Verb | Action | Description |
|-----|-----------|--------|-------------|
| /rest-auth/login/ | POST | create | Signs in existing user |
| /rest-auth/registration/ | POST | create | Registers new user |
| /portfolio/ | POST | create | Creates new Portfolio |
| /portfolio | GET | show | Lists all portfolios belonging to the current user |
| /portfolio/:id/transaction/ | POST | create | Creates new transaction |
| /porfolio/:id/transaction/ | GET | show | Lists all transactions from the portfolio |

### Models
#### Users:
The User model was generated with Django Rest-Auth framework and requires the parameters username, name, email and password. For authentication we used Rest-Auth's token authentication system. On registration, both email and username must be unique. 

#### Portfolios:
The portfolio model parameters include name, net earnings and owner. The owner is the user's id, which is input as the foreign key. Our program automatically inputs this value by retrieving the user id from the user database using the authentication token provided in the http request.

#### Transactions:
The transaction model is defined within portfolios as it is associated to a specific portfolio. The transaction parameters include ticker, instrument_name, number_of_shares, trade_date, close_out_date, buy_price, sell_price, net_earnings and portfolio_id. The portfolio_id, a foreign key, is retrieved from the RESTful routed http url.

## Set Up:

1. Clone this repo
2. Ensure you have python 3.9 downloaded on your system
3. Download pipenv from pythons package manager pip
4. In the root directory run `pipenv install` to install dependencies
5. run `pipenv shell` to activate your virtual environment
6. `cd lme_backend` to move into the lme_backend repository
7. run `python manage.py migrate` to create your databases
8. run `python manage.py createsuperuser` to create a user that has access to the admin panel of Django
9. run `python manage.py runserver` to run the server and navigate to [localhost](http://localhost:8000) or if your console signifies another port, navigate to that instead of 8000

## Technologies Used:

* Django
* Django Rest Framework
* Django Rest Auth
* SQLite
* Python

