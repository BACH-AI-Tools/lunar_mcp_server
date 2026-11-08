"""Tests for the Huangli / daily fortune Five Elements output (issue #4)."""

import server
from utils.lunar_helper import LunarHelper


def test_get_huangli_wu_xing_is_five_elements_not_gan_zhi():
    # 2024-01-01 is a 甲子 day: 甲 is Wood (木), 子 is Water (水).
    result = LunarHelper.get_huangli(2024, 1, 1)

    assert result["success"] is True
    assert result["gan_zhi_day"] == "甲子"
    assert result["wu_xing"] == "木水"
    assert set(result["wu_xing"]) <= set("金木水火土")


def test_get_huangli_reports_lucky_directions():
    result = LunarHelper.get_huangli(2024, 1, 1)

    assert result["position_xi"] == "东北"
    assert result["position_fu"] == "正北"
    assert result["position_cai"] == "东北"


def test_huangli_query_prints_five_elements():
    output = server.huangli_query("2024-01-01")

    assert "Wu Xing / 五行: 木水" in output
    assert "Wu Xing / 五行: 甲子" not in output


def test_fortune_daily_has_no_placeholder_text():
    output = server.fortune_daily("2024-01-01")

    assert "Five Element / 五行: 木水" in output
    assert "喜神东北" in output
    assert "财神东北" in output
    assert "根据甲子推算" not in output
    assert "根据五行" not in output


def test_wuxing_analyze_recommendations_heading_is_closed_bold():
    output = server.wuxing_analyze("1990-01-01", "08:30")

    assert "💡 **Recommendations / 建议:**" in output
