
## I've completed the below tasks and reordered them in the order I completed them with some additional detail

**i) Create a virtual environment and install the requirements - "requirements\requirements.txt"**

Implementation: Before starting any task, I created a venv using Python standard venv and installed the requirements

**ii) Create data models - example with sqlalchemy in "app\models.py"**
Implementation: I attempted this task first, by first changing configurations for sqlite and then creating models and schemas

**iii) Design a database mock up based on the provided data - "app\data\business_symptom_data.csv"**
Implementation: Once I defined the models, I designed a database mockup provided below:


  | Business       |         |
  | -------------- | ------- |
  | id (PK)        | name    |

  | Symptom        |         |            |
  | -------------- | ------- | ---------- |
  | code (PK)      | name    | diagnostic |

  | BusinessSymptom|         |
  | -------------- | ------- |
  | business_id (FK)| symptom_code (FK) |



**iv) Generate migration script and run migration to create database tables - alembic files provided**
  - To create a migration file: "alembic revision --autogenerate -m some_comment"
  - To update database with migration file: "alembic upgrade head"

Implementation: I wrote init_db.py file and ran alembic commands as well as init_db.py file in order to initiate the db. You can use 'python init_db.py' to run it.

**v) Create an endpoint for importing a CSV file into the database**
  - The only requirement is the endpoint requires a CSV file. If needed, other parameters can be used.

Implementation: I wrote csv import endpoint first and ensure that this endpoint is correctly importing the csv data and loading it into the db

**vi) Create an endpoint that returns business and symptom data**
  - Endpoint should take two optional parameters - business_id & diagnostic
  - Endpoint should return Business ID, Business Name, Symptom Code, Symptom Name, and Symptom Diagnostic values based on filter

Implementation: I wrote this endpoint at the end. After using csv import endpoint to import the data I implemented and tested this endpoint to ensure that everything was working as expected.



The final end result contains a filled database, two working APIs, and an accessible API docs page.
