import pytest
from deepchecks.tabular import Dataset
from deepchecks.tabular.suites import full_suite, data_integrity

from tests.test_utils.utils import load_real_gtzan_dataset, load_real_mfcc_dataset


class TestDataIntegrity:

    @pytest.fixture
    def setup(self):
        pass

    def test_dataset_gtzan_integrity(self):

        dataset = load_real_gtzan_dataset()

        if dataset:
            suite = data_integrity()
            suite_result = suite.run(dataset)
            suite_result.save_as_html("reports/tests/deep_gtzan_checks.html")
            with open('reports/tests/deep_checks.json', 'w+') as f:
                f.write(suite_result.to_json())

    def test_dataset_mfcc_integrity(self):

        dataset = load_real_mfcc_dataset()

        if dataset:
            suite = data_integrity()
            suite_result = suite.run(dataset)
            suite_result.save_as_html("reports/tests/deep_mfcc_checks.html")
            with open('reports/tests/deep_checks.json', 'w+') as f:
                f.write(suite_result.to_json())
