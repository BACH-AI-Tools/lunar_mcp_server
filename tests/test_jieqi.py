"""Tests for the 24 solar terms query (issue #3)."""

import re

import pytest

import server
from utils.lunar_helper import LunarHelper

# Solar term dates for 2024 (China Standard Time).
JIE_QI_2024 = [
    ("小寒", "2024-01-06"),
    ("大寒", "2024-01-20"),
    ("立春", "2024-02-04"),
    ("雨水", "2024-02-19"),
    ("惊蛰", "2024-03-05"),
    ("春分", "2024-03-20"),
    ("清明", "2024-04-04"),
    ("谷雨", "2024-04-19"),
    ("立夏", "2024-05-05"),
    ("小满", "2024-05-20"),
    ("芒种", "2024-06-05"),
    ("夏至", "2024-06-21"),
    ("小暑", "2024-07-06"),
    ("大暑", "2024-07-22"),
    ("立秋", "2024-08-07"),
    ("处暑", "2024-08-22"),
    ("白露", "2024-09-07"),
    ("秋分", "2024-09-22"),
    ("寒露", "2024-10-08"),
    ("霜降", "2024-10-23"),
    ("立冬", "2024-11-07"),
    ("小雪", "2024-11-22"),
    ("大雪", "2024-12-06"),
    ("冬至", "2024-12-21"),
]


def test_get_jie_qi_list_returns_all_24_terms_with_real_dates():
    result = LunarHelper.get_jie_qi_list(2024)

    assert result["success"] is True
    assert result["total_count"] == 24
    assert [
        (jq["name"], jq["solar_date"]) for jq in result["jie_qi_list"]
    ] == JIE_QI_2024
    assert all(
        jq["month"] == int(jq["solar_date"][5:7]) for jq in result["jie_qi_list"]
    )


@pytest.mark.parametrize("year", [1901, 1999, 2000, 2023, 2033, 2099])
def test_get_jie_qi_list_stays_within_the_requested_year(year):
    result = LunarHelper.get_jie_qi_list(year)

    assert result["total_count"] == 24
    dates = [jq["solar_date"] for jq in result["jie_qi_list"]]
    assert dates == sorted(dates)
    assert all(d.startswith(f"{year}-") for d in dates)
    assert result["jie_qi_list"][0]["name"] == "小寒"
    assert result["jie_qi_list"][-1]["name"] == "冬至"


def test_jieqi_query_tool_lists_24_terms():
    output = server.jieqi_query(2024)

    assert "Total Count / 总数:** 24" in output
    assert "立春 - 2024-02-04" in output
    assert "No solar terms found" not in output
    assert len(re.findall(r"^\s*\d+\. ", output, flags=re.M)) == 24
