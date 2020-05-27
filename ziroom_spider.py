import requests
from bs4 import BeautifulSoup
from lxml import etree


def get_zi_room_info(url):
    response = requests.get(url)
    response.encoding = "utf8"
    print(response)
    parser = BeautifulSoup(response.text, "html.parser")

    name = parser.find(class_='Z_name').text

    area_and_type = parser.find(class_='Z_home_b clearfix').text.split()
    area = area_and_type[0]
    room_type = area_and_type[4]

    location_and_floor = parser.find(class_='Z_home_o').text.split()
    location = location_and_floor[1]
    floor = location_and_floor[2][2:]
    elevator = location_and_floor[3]
    age = location_and_floor[4]
    heater = location_and_floor[5]

    z_tags = parser.find(class_='Z_tags').text.split()
    style = z_tags[0]
    is_code_lock = z_tags[1]
    is_first = z_tags[2]
    near_metro = z_tags[3]
    print('房源: ' + name)
    print('面积: ' + area)
    print('户型: ' + room_type)
    print('位置: ' + location)
    print('楼层: ' + floor)
    print('电梯: ' + elevator)
    print('年代: ' + age)
    print('供暖: ' + heater)
    print('装修风格: ' + style)
    print('是否智能锁: ' + is_code_lock)
    print('是否首次出租: ' + is_first)
    print('是否离地铁近: ' + near_metro)


if __name__ == '__main__':
    get_zi_room_info("http://www.ziroom.com/x/744536289.html")
