import pandas as pd
from pipeline.model import RawDataModel, ProcessedDataModel


class RawDataModelAggregator:
    def aggregate(self, raw_data_models: list[RawDataModel]) -> pd.DataFrame:
        dataframe = pd.DataFrame([dict(model) for model in raw_data_models])
        groups = dataframe.groupby(
            ["name", pd.Grouper(key="timestamp", freq="15min", label="left")]
        )

        aggregates = groups.aggregate(
            average_temperature=pd.NamedAgg(column="temperature", aggfunc="mean"),
            min_temperature=pd.NamedAgg(column="temperature", aggfunc="min"),
            max_temperature=pd.NamedAgg(column="temperature", aggfunc="max"),
        )

        return aggregates.reset_index()
