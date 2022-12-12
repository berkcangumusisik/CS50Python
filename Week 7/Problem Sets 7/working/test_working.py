import pytest
from working import convert


def test_time_case():
    assert convert("9:00 AM to 5:00 PM") == "09:00 to 17:00"


def test_max_range():
    assert convert("12:00 PM to 12:00 PM") == "12:00 to 12:00"


def test_mixed_formats():
    with pytest.raises(ValueError):
        convert("09:00 to 17:00")


def test_omit_to():
    with pytest.raises(ValueError):
        convert(" to ")


def test_out_of_range_hours():
    with pytest.raises(ValueError):
        convert("13:00 AM to 13:00 PM")

    with pytest.raises(ValueError):
        convert("0:00 AM to 0:00 PM")

    with pytest.raises(ValueError):
        convert("13 AM to 13 PM")

    with pytest.raises(ValueError):
        convert("0 AM to 0 PM")


def test_out_of_range_minutes():
    with pytest.raises(ValueError):
        convert("12:61 AM to 5:60 PM")


def test_no_entry():
    with pytest.raises(ValueError):
        convert("")


def test_invalid_format():
    with pytest.raises(ValueError):
        convert("9AM to 5PM")

    with pytest.raises(ValueError):
        convert("6:19 AM 4:20 PM")

    with pytest.raises(ValueError):
        convert("9 AM - 5 PM")