# loan-mini

An App to mimic Loan Requesting, Approval and Payment process. 

# Considerations
1. Used PSQL, but can be run using sqlite db as well. 
2. Using "Basic Auth" and django-rest-framework for authentication and request/response json wrapping.
3. There are two types of user in the System, "Staff" and "Customer". 
4. Staff --> set `is_staff=True` in SignUp API
5. Customer --> set `is_staff=False` in SignUp API
6. Auth Credentials --> Email + Password passed during SignUp
7. All the APIs can be found in `core/urls.py` file, along with basic comments. 


# Setup Codebase

## Create a Virtual Env
`python -m venv venv`

## Activate Virtual Env
`source ./venv/activate`

## Install Requirements
`pip install -r requirements.txt`

## Update Config File with Database details
### File Location : env/.dev
### Keys to Update
```
DB_NAME="psql database" [make sure its already created before starting the server]
DB_USERNAME="psql username"
DB_PASS="psql password"
```

## Run Migrations
`python manage.py migrate`

## Start Server
`python manage.py runserver`


# How to Test
There are two ways to test. 
1. Running Unit Tests
2. Hitting server using postman

## Running Unit Tests
If the server and database is setup, then the tests can be run with the following command 

`python manage.py test`

Tests are located in `core/tests_core/test_loan.py` file. 

## Using Postman
Link to Postman Collection : I have added a JSON of the Postman Collection with the Codebase. 

It supports the following APIs
1. Create User / SignUp
2. Test Login (Tests if Basic Authentication is working )
3. Create Loan
4. List All Loans (If "STAFF" User is passed)
5. List User Loans (If a "Customer" User is passed)
6. Approve Loan (Can only be called through STAFF user credentials)
7. Deny Loan (Can only be called through STAFF user credentials)
8. Pay Loan (Called from Customer Credentials)


