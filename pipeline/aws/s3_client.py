from __future__ import annotations

import json
from typing import Any, TYPE_CHECKING


if TYPE_CHECKING:
    from mypy_boto3_s3 import S3Client as BotoClient


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
