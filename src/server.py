#!/usr/bin/env python3
"""
Lunar Calendar MCP Server / 农历MCP服务器

A Model Context Protocol server for Chinese traditional calendar functions
中国传统历法功能的模型上下文协议服务器
"""

from mcp.server import FastMCP
from utils.lunar_helper import LunarHelper

# Initialize the MCP server / 初始化MCP服务器
app = FastMCP(
    name="lunar-calendar",
    instructions="Chinese Lunar Calendar MCP Server - 农历MCP服务器"
)


@app.tool()
def bazi_calculate(birth_date: str, birth_time: str) -> str:
    """
    Calculate BaZi (Eight Characters) for fortune telling / 计算生辰八字用于算命

    Args:
        birth_date: Birth date in YYYY-MM-DD format / 出生日期，格式YYYY-MM-DD
        birth_time: Birth time in HH:MM format / 出生时间，格式HH:MM

    Returns:
        Detailed BaZi calculation result / 详细的八字计算结果
    """
    try:
        date_parts = birth_date.split("-")
        time_parts = birth_time.split(":")

        year, month, day = int(date_parts[0]), int(date_parts[1]), int(date_parts[2])
        hour, minute = int(time_parts[0]), int(time_parts[1]) if len(time_parts) > 1 else 0

        result = LunarHelper.get_bazi(year, month, day, hour, minute)

        if result["success"]:
            output = f"""🎋 **BaZi Calculation Result / 生辰八字计算结果**

📅 **Birth Info / 出生信息:**
- Date & Time / 出生时间: {result['birth_datetime']}
- Zodiac / 生肖: {result['zodiac']}

🔮 **Eight Characters / 八字:**
- Year Pillar / 年柱: {result['year_gan_zhi']}
- Month Pillar / 月柱: {result['month_gan_zhi']}
- Day Pillar / 日柱: {result['day_gan_zhi']}
- Hour Pillar / 时柱: {result['hour_gan_zhi']}

**Complete BaZi / 完整八字:** {result['bazi_string']}

🌟 **Five Elements / 五行:**
- Year / 年: {result['wu_xing']['year']}
- Month / 月: {result['wu_xing']['month']}
- Day / 日: {result['wu_xing']['day']}
- Hour / 时: {result['wu_xing']['hour']}

🎵 **Na Yin / 纳音:**
- Year / 年: {result['na_yin']['year']}
- Month / 月: {result['na_yin']['month']}
- Day / 日: {result['na_yin']['day']}
- Hour / 时: {result['na_yin']['hour']}
"""
        else:
            output = f"❌ **Error / 错误:** {result['error']}"

        return output

    except Exception as e:
        return f"Error parsing date/time / 日期时间解析错误: {str(e)}"
@app.tool()
def calendar_convert(date: str, convert_to: str, is_leap: bool = False) -> str:
    """
    Convert between solar and lunar calendar / 公历农历互转

    Args:
        date: Date in YYYY-MM-DD format / 日期，格式YYYY-MM-DD
        convert_to: Convert to "lunar" or "solar" / 转换为"lunar"或"solar"
        is_leap: Is leap month (only for lunar to solar conversion) / 是否闰月（仅用于农历转公历）

    Returns:
        Calendar conversion result / 历法转换结果
    """
    if not date or not convert_to:
        return "Missing date or convert_to parameter / 缺少日期或转换类型参数"

    try:
        date_parts = date.split("-")
        year, month, day = int(date_parts[0]), int(date_parts[1]), int(date_parts[2])

        if convert_to == "lunar":
            result = LunarHelper.solar_to_lunar(year, month, day)

            if result["success"]:
                output = f"""🌙 **Calendar Conversion / 历法转换**

📅 **Solar Date / 公历日期:** {result['solar_date']}
🏮 **Lunar Date / 农历日期:** {result['lunar_date_chinese']}

📊 **Detailed Info / 详细信息:**
- Lunar Year / 农历年: {result['lunar_year']} ({result['lunar_year_chinese']})
- Lunar Month / 农历月: {result['lunar_month']} ({result['lunar_month_chinese']})
- Lunar Day / 农历日: {result['lunar_day']} ({result['lunar_day_chinese']})
- Is Leap Month / 是否闰月: {'是' if result['is_leap_month'] else '否'}

🐲 **Zodiac & Stems / 生肖干支:**
- Zodiac / 生肖: {result['zodiac']}
- Year Gan Zhi / 年干支: {result['gan_zhi_year']}
- Month Gan Zhi / 月干支: {result['gan_zhi_month']}
- Day Gan Zhi / 日干支: {result['gan_zhi_day']}

🌸 **Solar Term / 节气:** {result['jie_qi'] or '无'}
📆 **Weekday / 星期:** {result['week_chinese']}
"""
            else:
                output = f"❌ **Error / 错误:** {result['error']}"

        elif convert_to == "solar":
            result = LunarHelper.lunar_to_solar(year, month, day, is_leap)

            if result["success"]:
                output = f"""☀️ **Calendar Conversion / 历法转换**

🏮 **Lunar Date / 农历日期:** {result['lunar_date']} {'(闰月)' if result['is_leap_month'] else ''}
📅 **Solar Date / 公历日期:** {result['solar_date']}

📊 **Detailed Info / 详细信息:**
- Solar Year / 公历年: {result['solar_year']}
- Solar Month / 公历月: {result['solar_month']}
- Solar Day / 公历日: {result['solar_day']}
- Weekday / 星期: {result['week_chinese']}
"""
            else:
                output = f"❌ **Error / 错误:** {result['error']}"
        else:
            output = "❌ **Invalid convert_to parameter / 无效的转换类型参数**"

        return output

    except Exception as e:
        return f"Error parsing date / 日期解析错误: {str(e)}"


@app.tool()
def huangli_query(date: str) -> str:
    """
    Query Chinese almanac (Huangli) for a specific date / 查询指定日期的黄历信息

    Args:
        date: Date in YYYY-MM-DD format / 日期，格式YYYY-MM-DD

    Returns:
        Detailed almanac information / 详细的黄历信息
    """
    if not date:
        return "Missing date parameter / 缺少日期参数"

    try:
        date_parts = date.split("-")
        year, month, day = int(date_parts[0]), int(date_parts[1]), int(date_parts[2])

        result = LunarHelper.get_huangli(year, month, day)

        if result["success"]:
            yi_list = result.get('yi', [])
            ji_list = result.get('ji', [])
            festivals = result.get('festivals', []) + result.get('other_festivals', [])

            output = f"""📅 **Chinese Almanac / 黄历查询**

📅 **Date / 日期:** {result['date']}
🏮 **Lunar Date / 农历:** {result['lunar_date_chinese']}
📆 **Weekday / 星期:** {result['week_chinese']}

🐲 **Zodiac & Stems / 生肖干支:**
- Zodiac / 生肖: {result['zodiac']}
- Year Gan Zhi / 年干支: {result['gan_zhi_year']}
- Month Gan Zhi / 月干支: {result['gan_zhi_month']}
- Day Gan Zhi / 日干支: {result['gan_zhi_day']}

✅ **Suitable Activities / 宜:**
{', '.join(yi_list) if yi_list else '无特别适宜事项'}

❌ **Unsuitable Activities / 忌:**
{', '.join(ji_list) if ji_list else '无特别禁忌事项'}

🌸 **Solar Term / 节气:** {result.get('jie_qi', '无')}
🎉 **Festivals / 节日:** {', '.join(festivals) if festivals else '无'}

🔮 **Metaphysical Info / 玄学信息:**
- Wu Xing / 五行: {result.get('wu_xing', '无')}
- Chong / 冲: {result.get('chong', '无')}
- Sha / 煞: {result.get('sha', '无')}
- Pengzu Taboo / 彭祖百忌: {result.get('pengzu_gan', '')} {result.get('pengzu_zhi', '')}
"""
        else:
            output = f"❌ **Error / 错误:** {result['error']}"

        return output

    except Exception as e:
        return f"Error parsing date / 日期解析错误: {str(e)}"


@app.tool()
def fortune_daily(date: str) -> str:
    """
    Get daily fortune and recommendations / 获取每日运势和建议

    Args:
        date: Date in YYYY-MM-DD format / 日期，格式YYYY-MM-DD

    Returns:
        Daily fortune analysis / 每日运势分析
    """
    if not date:
        return "Missing date parameter / 缺少日期参数"

    try:
        date_parts = date.split("-")
        year, month, day = int(date_parts[0]), int(date_parts[1]), int(date_parts[2])

        result = LunarHelper.get_huangli(year, month, day)

        if result["success"]:
            yi_list = result.get('yi', [])
            ji_list = result.get('ji', [])

            output = f"""🔮 **Daily Fortune / 每日运势**

📅 **Date / 日期:** {result['date']}
🏮 **Lunar Date / 农历:** {result['lunar_date_chinese']}
🐲 **Zodiac / 生肖:** {result['zodiac']}

✨ **Today's Recommendations / 今日建议:**

✅ **Good for / 适宜:**
{', '.join(yi_list[:5]) if yi_list else '休息调养'}

❌ **Avoid / 避免:**
{', '.join(ji_list[:5]) if ji_list else '无特别禁忌'}

🌟 **Lucky Elements / 幸运元素:**
- Five Element / 五行: {result['wu_xing']}
- Direction / 方位: 喜神{result['position_xi']}, 福神{result['position_fu']}, 财神{result['position_cai']}

📈 **Fortune Index / 运势指数:**
- Overall / 综合: ⭐⭐⭐⭐ (基于黄历宜忌)
- Career / 事业: {'⭐⭐⭐⭐⭐' if '工作' in str(yi_list) else '⭐⭐⭐'}
- Love / 感情: {'⭐⭐⭐⭐⭐' if '嫁娶' in str(yi_list) else '⭐⭐⭐'}
- Wealth / 财运: {'⭐⭐⭐⭐⭐' if '交易' in str(yi_list) else '⭐⭐⭐'}

💡 **Daily Tip / 每日贴士:**
根据今日干支{result.get('gan_zhi_day', '')}，建议保持平和心态，顺应自然规律。
"""
        else:
            output = f"❌ **Error / 错误:** {result['error']}"

        return output

    except Exception as e:
        return f"Error parsing date / 日期解析错误: {str(e)}"


@app.tool()
def jieqi_query(year: int) -> str:
    """
    Query 24 solar terms (Jie Qi) for a year / 查询一年的二十四节气

    Args:
        year: Year to query / 查询的年份

    Returns:
        List of solar terms for the year / 该年的节气列表
    """
    if not year:
        return "Missing year parameter / 缺少年份参数"

    try:
        result = LunarHelper.get_jie_qi_list(year)

        if result["success"]:
            jie_qi_list = result.get("jie_qi_list", [])

            output = f"""🌸 **24 Solar Terms / 二十四节气查询**

📅 **Year / 年份:** {result['year']}
📊 **Total Count / 总数:** {result['total_count']}

🌱 **Solar Terms List / 节气列表:**
"""

            for i, jq in enumerate(jie_qi_list, 1):
                output += f"{i:2d}. {jq['name']} - {jq['solar_date']} (第{jq['month']}月)\n"

            if not jie_qi_list:
                output += "未找到节气信息 / No solar terms found"

        else:
            output = f"❌ **Error / 错误:** {result['error']}"

        return output

    except Exception as e:
        return f"Error processing year / 年份处理错误: {str(e)}"


@app.tool()
def wuxing_analyze(birth_date: str, birth_time: str) -> str:
    """
    Analyze Wu Xing (Five Elements) from birth info / 根据出生信息分析五行

    Args:
        birth_date: Birth date in YYYY-MM-DD format / 出生日期，格式YYYY-MM-DD
        birth_time: Birth time in HH:MM format / 出生时间，格式HH:MM

    Returns:
        Wu Xing analysis result / 五行分析结果
    """
    if not birth_date or not birth_time:
        return "Missing birth_date or birth_time / 缺少出生日期或时间"

    try:
        date_parts = birth_date.split("-")
        time_parts = birth_time.split(":")

        year, month, day = int(date_parts[0]), int(date_parts[1]), int(date_parts[2])
        hour, minute = int(time_parts[0]), int(time_parts[1]) if len(time_parts) > 1 else 0

        result = LunarHelper.analyze_wu_xing(year, month, day, hour, minute)

        if result["success"]:
            wu_xing_count = result["wu_xing_count"]
            dominant = result["dominant_elements"]
            missing = result["missing_elements"]
            weak = result["weak_elements"]

            output = f"""🧮 **Wu Xing Analysis / 五行分析**

📅 **Birth Info / 出生信息:** {result['birth_datetime']}

🌟 **Five Elements Count / 五行统计:**
- 金 (Metal): {wu_xing_count['金']}
- 木 (Wood): {wu_xing_count['木']}
- 水 (Water): {wu_xing_count['水']}
- 火 (Fire): {wu_xing_count['火']}
- 土 (Earth): {wu_xing_count['土']}

🎯 **Analysis Results / 分析结果:**

💪 **Dominant Elements / 旺相元素:**
{', '.join(dominant) if dominant else '无明显旺相元素'}

❌ **Missing Elements / 缺失元素:**
{', '.join(missing) if missing else '五行齐全'}

⚖️ **Weak Elements / 偏弱元素:**
{', '.join(weak) if weak else '无明显偏弱元素'}

🔮 **BaZi Wu Xing / 八字五行:**
- Year / 年柱: {result['bazi_wu_xing']['year']}
- Month / 月柱: {result['bazi_wu_xing']['month']}
- Day / 日柱: {result['bazi_wu_xing']['day']}
- Hour / 时柱: {result['bazi_wu_xing']['hour']}

📝 **Summary / 总结:**
{result['analysis_summary']}

💡 **Recommendations / 建议:**
"""

            if missing:
                output += f"- 建议补充缺失的{', '.join(missing)}元素\n"
            if dominant:
                output += f"- 注意平衡过旺的{', '.join(dominant)}元素\n"
            if not missing and not weak:
                output += "- 五行相对平衡，保持现状即可\n"

        else:
            output = f"❌ **Error / 错误:** {result['error']}"

        return output

    except Exception as e:
        return f"Error parsing date/time / 日期时间解析错误: {str(e)}"


def main():
    """Main function to run the MCP server / 运行MCP服务器的主函数"""
    # FastMCP.run() handles everything: stdio transport, async event loop, etc.
    app.run()


if __name__ == "__main__":
    main()
