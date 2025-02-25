import pandas as pd
from pipeline.model import RawDataModel


class RawDataModelAggregator:
    def aggregate(self, raw_data_models: list[RawDataModel]) -> pd.DataFrame:
        dataframe = pd.DataFrame([dict(model) for model in raw_data_models])
        dataframe["timestamp"] = pd.to_datetime(dataframe["timestamp"])

        groups = dataframe.groupby(["name", pd.Grouper(key="timestamp", freq="15min")])

        aggregates = groups.aggregate(
            average_temperature=pd.NamedAgg(column="temperature", aggfunc="mean"),
            min_temperature=pd.NamedAgg(column="temperature", aggfunc="min"),
            max_temperature=pd.NamedAgg(column="temperature", aggfunc="max"),
        )

        return aggregates.reset_index()
