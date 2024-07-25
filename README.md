# etl-pipeline-demo
A demonstration to showcase how to do an extract-transform-load pipeline to bring data from s3 into a Postgres database

## Developer Setup

- Python 3.12
- [Poetry](https://python-poetry.org/)
- Node.js
- postgres

Node.js is mainly used to deploy the infrastructure with cdk.

Install dependencies:

- Go to the `./infrastructure` folder and run `npm install`.
- Go to the `pipeline` folder and run `poetry install`.

