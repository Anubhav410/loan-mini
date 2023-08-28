# loan-mini

An App to mimic Loan Requesting, Approval and Payment process. 

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
