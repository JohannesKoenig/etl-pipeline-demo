# etl-pipeline-demo
A demonstration to showcase how to do an extract-transform-load pipeline to bring data from s3 into a Postgres database.
This is based on skills acquired in previous jobs and was not run against AWS for the lack of an enterprise AWS account.

## Developer Setup

- Python 3.12
- [Poetry](https://python-poetry.org/)
- Node.js
- postgres

Node.js is mainly used to deploy the infrastructure with cdk.

Install dependencies:

- Go to the `./infrastructure` folder and run `npm install`.
- Go to the `pipeline` folder and run `poetry install`.

Formatting:

For the python project go to the `pipeline` folder and execute 
```poetry run ruff format```
to format the project. You can run static typechecking with
```poetry run pyright```

Database setup:

The `sql` folder stores files for initializing the postgres database.
Use the `table.psql` to create the `processed_data` table.