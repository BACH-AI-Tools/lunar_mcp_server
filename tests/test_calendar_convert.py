"""Tests for solar -> lunar conversion of leap-month dates (issue #6)."""

import server
from utils.lunar_helper import LunarHelper


def test_solar_to_lunar_reports_positive_month_for_leap_month():
    # 2023-03-22 is the 1st day of the leap 2nd lunar month (闰二月初一).
    result = LunarHelper.solar_to_lunar(2023, 3, 22)

    assert result["success"] is True
    assert result["lunar_month"] == 2
    assert result["is_leap_month"] is True
    assert result["lunar_month_chinese"] == "闰二"
    assert result["lunar_day"] == 1


def test_solar_to_lunar_regular_month_is_not_leap():
    # 2023-02-20 is the 1st day of the regular 2nd lunar month (二月初一).
    result = LunarHelper.solar_to_lunar(2023, 2, 20)

    assert result["lunar_month"] == 2
    assert result["is_leap_month"] is False
    assert result["lunar_month_chinese"] == "二"


def test_calendar_convert_does_not_print_negative_month():
    output = server.calendar_convert("2023-03-22", "lunar")

    assert "Lunar Month / 农历月: 2 (闰二)" in output
    assert "Is Leap Month / 是否闰月: 是" in output
    assert "农历月: -" not in output


def test_leap_month_round_trip():
    lunar = LunarHelper.solar_to_lunar(2023, 3, 22)
    solar = LunarHelper.lunar_to_solar(
        lunar["lunar_year"],
        lunar["lunar_month"],
        lunar["lunar_day"],
        is_leap=lunar["is_leap_month"],
    )

    assert solar["solar_date"] == "2023-03-22"
