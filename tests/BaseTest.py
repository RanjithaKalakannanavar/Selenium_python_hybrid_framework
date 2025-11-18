from datetime import datetime

import pytest


@pytest.mark.usefixtures("setup_and_teardown","log_on_failure")
class BaseTest:
    pass

    '''def provide_time_stamp(self):
        utc_time=datetime.now().strftime("%M_%D_%Y%H_%M_%S")
        return 'ranjitha'+utc_time+'@gmail.com'''