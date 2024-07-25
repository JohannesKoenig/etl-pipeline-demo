from pydantic import BaseModel


class RawDataModel(BaseModel):
    external_id: str
    temperature: float
    humidity: float
    wind_speed: float
    name: str
    timestamp: str


class ProcessedDataModel(BaseModel):
    average_temperature: float
    min_temperature: float
    max_temperature: float
    timestamp: str
    name: str


class RawDataFile(BaseModel):
    raw_data_models: list[RawDataModel]
