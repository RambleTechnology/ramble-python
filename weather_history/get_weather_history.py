import requests
import csv
import re
import os
from lxml import etree
import pyecharts.options as opts
from pyecharts.charts import Line

# 设置请求头
headers = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36 Edg/127.0.0.0",
}


def input_data():
    """输入地点，时间"""
    city = input("请输入查询城市：")
    month = input("请输入查询月份（格式：202307）：")
    return city, month


def get_date_url(city, month):
    """获取当月日期地址"""
    if os.path.exists("city_data.csv"):
        with open("city_data.csv", mode="r", encoding="utf-8") as f:
            reader = csv.reader(f)
            for row in reader:
                if city == row[0]:
                    city_id = row[1]
    month_url = f"https://lishi.tianqi.com/{city_id}/{month}.html"
    return month_url


def extract_numbers(string):
    """提取字符串中的数字"""
    numbers = re.findall(r"-?\d+", string)[0]
    return float(numbers)


def spider_weather(date_url, city, month):
    try:
        response = requests.get(url=date_url, headers=headers)
        html = etree.HTML(response.text)
        tree = html.xpath("/html/body/div[7]/div[1]/div[4]/ul/li")
        date_name_list = []
        high_temperatures = []
        low_temperatures = []
        weathers = []
        for i in tree:
            date = i.xpath("./div[1]/text()")[0].split(" ")[0]
            high_temperature = extract_numbers(i.xpath("./div[2]/text()")[0])
            low_temperature = extract_numbers(i.xpath("./div[3]/text()")[0])
            weather = i.xpath("./div[4]/text()")[0]
            wind = i.xpath("./div[5]/text()")[0]
            print(date, high_temperature, low_temperature, weather, wind)
            date_name_list.append(date)
            high_temperatures.append(high_temperature)
            low_temperatures.append(low_temperature)
            weathers.append(weather)

        line = (
            Line(
                init_opts=opts.InitOpts(
                    width="1200px", height="600px", page_title="月份气温折线图"
                )
            )
            .add_xaxis(xaxis_data=date_name_list)
            .add_yaxis(
                series_name="最高气温",
                y_axis=high_temperatures,
                markpoint_opts=opts.MarkPointOpts(
                    data=[
                        opts.MarkPointItem(type_="max", name="最大值"),
                    ]
                ),
                markline_opts=opts.MarkLineOpts(
                    data=[opts.MarkLineItem(type_="average", name="平均值")]
                ),
            )
            .add_yaxis(
                series_name="最低气温",
                y_axis=low_temperatures,
                markpoint_opts=opts.MarkPointOpts(
                    data=[opts.MarkPointItem(type_="min", name="最小值")]
                ),
                markline_opts=opts.MarkLineOpts(
                    data=[
                        opts.MarkLineItem(type_="average", name="平均值"),
                    ]
                ),
            )
            .set_global_opts(
                # 设置主副标题
                title_opts=opts.TitleOpts(
                    title=f"{city}地区{month[0:4]}年{month[4:]}月气温走势折线图",
                    subtitle=f"{city}",
                ),
                tooltip_opts=opts.TooltipOpts(trigger="axis"),
                toolbox_opts=opts.ToolboxOpts(
                    is_show=True,
                    feature=opts.ToolBoxFeatureOpts(
                        save_as_image=opts.ToolBoxFeatureSaveAsImageOpts(
                            pixel_ratio=3, type_="jpg", background_color="#fff"
                        )
                    ),
                ),
                xaxis_opts=opts.AxisOpts(
                    type_="category",
                    boundary_gap=False,
                    name="日期",
                    min_=0,
                    max_=len(date_name_list),
                    axisline_opts=opts.AxisLineOpts(symbol=["none", "arrow"]),
                ),
                datazoom_opts=opts.AxisLineOpts(),
            )
        )
        line.render(f"{city}地区{month[0:4]}年{month[4:]}月气温走势折线图.html")
    except Exception as e:
        print(e)


def main():
    city, month = input_data()
    month_url = get_date_url(city, month)
    spider_weather(month_url, city, month)


if __name__ == "__main__":
    main()
