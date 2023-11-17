from lib.contact import *
import pytest

def test_contact_initialises():
    contact1 = Contact("Jane Doe", "+447777777777")
    assert contact1.name == "Jane Doe"
    assert contact1.number == "+447777777777"

# def test_error_with_invalid_input():
#     with pytest.raises(Exception) as e:
#         contact1 = Contact(123, "0756")
#     error = str(e.value)
#     assert error == "invalid data"

#     with pytest.raises(Exception) as e2:
#         contact2 = Contact('', 756)
#     error = str(e2.value)
#     assert error == "invalid data"

#     with pytest.raises(Exception) as e3:
#         contact3 = Contact("Jane", '')
#     error = str(e3.value)
#     assert error == "invalid data"