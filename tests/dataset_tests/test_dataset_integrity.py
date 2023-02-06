import json

import pytest
from deepchecks.tabular import Dataset
from deepchecks.tabular.suites import data_integrity

from tests.testUtils import load_real_dataset


class TestDataIntegrity:

    @pytest.fixture
    def setup(self):
        pass

    def test_dataset_integrity(self):
        dataset, _, _ = load_real_dataset()
        feature_cols = list(dataset.columns.values).remove("label")

        dataset_test = Dataset(dataset,
                               features=feature_cols,
                               label='label')
        integ_suite = data_integrity()
        suite_result = integ_suite.run(dataset_test)
            with open('data.json', 'w+') as f:
            json.dump(suite_result.to_json(), f)


TestDataIntegrity().test_dataset_integrity()