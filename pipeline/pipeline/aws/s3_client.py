from __future__ import annotations
from typing import Any, TYPE_CHECKING

import json
import boto3


if TYPE_CHECKING:
    from mypy_boto3_s3 import S3Client as BotoClient


def get_boto_client() -> BotoClient:
    return boto3.client("s3")


class S3Client:
    def __init__(self, boto_client: BotoClient):
        self._client = boto_client

    def get_object(self, bucket: str, key: str) -> Any:
        try:
            response = self._client.get_object(Bucket=bucket, Key=key)
        except self._client.exceptions.NoSuchKey:
            raise ObjectNotFound()
        body = response["Body"]
        return json.load(body)


class ObjectNotFound(Exception):
    pass
