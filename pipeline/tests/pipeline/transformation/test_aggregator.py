import pandas as pd
from pipeline.model import RawDataModel
from pipeline.transformation.aggregator import RawDataModelAggregator


class TestRawDataModelAggregator:
    def test_aggregate(self):
        # Given
        raw_data = [
            RawDataModel(
                external_id="1",
                temperature=0.0,
                humidity=1.0,
                wind_speed=1.0,
                name="name",
                timestamp="2024-01-01T00:00:00Z",
            ),
            RawDataModel(
                external_id="2",
                temperature=2.0,
                humidity=1.0,
                wind_speed=1.0,
                name="name",
                timestamp="2024-01-01T00:01:00Z",
            ),
        ]
        aggregator = RawDataModelAggregator()

        result = aggregator.aggregate(raw_data)
        expected = pd.DataFrame(
            {
                "name": ["name"],
                "timestamp": [
                    "2024-01-01T00:00:00Z",
                ],
                "average_temperature": [1.0],
                "min_temperature": [0.0],
                "max_temperature": [2.0],
            }
        )
        expected["timestamp"] = pd.to_datetime(expected["timestamp"])
        pd.testing.assert_frame_equal(result, expected)
