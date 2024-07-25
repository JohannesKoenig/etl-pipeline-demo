from typing import Any
import os
import logging
from pipeline.aws.s3_client import S3Client, get_boto_client
from pipeline.model import RawDataFile
from pipeline.transformation.aggregator import RawDataModelAggregator
from pipeline.database.database_client import DatabaseClient, get_database_connection

DATA_SET_FILE = "data_set.json"
LOG = logging.getLogger()
LOG.setLevel(logging.DEBUG)


def handler(_event: dict[str, Any], _context: Any) -> None:
    s3_client = S3Client(get_boto_client())
    raw_file_content = s3_client.get_object(get_bucket_name(), DATA_SET_FILE)
    raw_data_file = RawDataFile.model_validate(raw_file_content)
    LOG.info(f"Received {len(raw_data_file.raw_data_models)} raw data models")

    aggregator = RawDataModelAggregator()
    aggregate = aggregator.aggregate(raw_data_file.raw_data_models)

    database_client = DatabaseClient(
        get_database_connection(
            host=get_database_host(),
            port=get_database_port(),
            user=get_database_user(),
            password=get_database_password(),
            database=get_database_name(),
        )
    )
    database_client.write_dataframe(aggregate)


def get_bucket_name() -> str:
    return os.environ["BUCKET_NAME"]


def get_database_host() -> str:
    return os.environ["DATABASE_HOST"] or "postgres.local"


def get_database_port() -> str:
    return os.environ["DATABASE_PORT"] or "5432"


def get_database_user() -> str:
    return os.environ["DATABASE_USER"] or "postgres"


def get_database_password() -> str:
    return os.environ["DATABASE_PASSWORD"] or "password"


def get_database_name() -> str:
    return os.environ["DATABASE_NAME"] or "database"
