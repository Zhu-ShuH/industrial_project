"""正常记录、边界值和非法输入的回归测试。"""

import pytest

from plantops import parse_reading


@pytest.mark.parametrize("value", ["0", "-273.15", "120"])
def test_temperature_boundaries(value):
    assert parse_reading(f"DEV-01:{value}")["temperature"] == float(value)


@pytest.mark.parametrize(
    "text", ["DEV-1:3", "missing_separator", "DEV-01:nan", "DEV-01:inf", "DEV-01:x"]
)
def test_invalid_input(text):
    with pytest.raises(ValueError):
        parse_reading(text)


def test_strip_outer_whitespace():
    assert parse_reading("  DEV-02:36.5  ")["device_id"] == "DEV-02"
