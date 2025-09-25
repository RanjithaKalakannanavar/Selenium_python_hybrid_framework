import pytest


@pytest.mark.usefixtures("setup_and_teardown")
class test_data_driven_testing:
    def data_driven_test(self):
