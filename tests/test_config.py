# In that File Always Define Function With test Name
import pytest


class NotInRange(Exception):
    def __init__(self, message="Value Not In Range"):
        self.message = message
        super().__init__(self.message)


def test_generic():
    a = 5
    with pytest.raises(NotInRange):
        if a not in range(10, 6):
            raise NotInRange