#coding: utf-8
import random
import numpy as np

list = ['https://t.co/EIHzNVbfAb',
        'https://t.co/YUfRnpCz9o',
        'https://t.co/GzPWfBaeBa',
        'https://t.co/YPWkBIWth2',
        'https://t.co/2LavPSkwyN',
        'https://t.co/0GxmLNV1wW',
        'https://t.co/C19bI7VLIc',
        'https://t.co/2M6asqBHYU',
        'https://t.co/4F9VsscUeG',
        'https://t.co/O73vmc5ohw',
        'https://t.co/Tl5T0B5DTY',
        'https://t.co/DqQ9uT5TNz',
        'https://t.co/O9ISG32l5U',
        'https://t.co/NVXSR7oLQi',
        'https://t.co/Du0TDPQ0Us',
        'https://t.co/HB2OR4Fh4V',
        'https://t.co/FoUgd7LrZF',
        'https://t.co/rra5VzKxCP',
        'https://t.co/xBJa8BtspZ',
        'https://t.co/hZbKl00xw4',
        'https://t.co/fex9mSuLej',
        'https://t.co/KKyVCnpGOT',
        'https://t.co/kH06I5nUmF',
        'https://t.co/PetQxbADaA',
        'https://t.co/A2LXWvpH6A',
        'https://t.co/wZKoxHl8Kx',
        'https://t.co/7sGprlIvjc',
        'https://t.co/0TyEVZMdzt',
        'https://t.co/m4H7jysfhl',
        'https://t.co/iuIGooqfjw',
        'https://t.co/ccUj87VlCD',
        'https://t.co/p08eI8O5dJ',
        'https://t.co/AOm9zoL7KL',
        'https://t.co/5yzSgIOKUy',
        'https://t.co/YQmuHa6OcY',
        'https://t.co/nigDixcHev',
        'https://t.co/IaQ91Bvzq9',
        'https://t.co/aqY3JB8RfF',
        'https://t.co/5HlAwxm8Fx',
        'https://t.co/3WJSYVoIZM',
        'https://t.co/hwYLvrnbOz',
        'https://t.co/0SLNCGIZhx',
        'https://t.co/0daABcI5Cv',
        'https://t.co/Ue83YMALuK',
        'https://t.co/LprX5hjGYl',
        'https://t.co/iHG4WfrC52',
        'https://t.co/PGlqTHW6LP',
        'https://t.co/pOt39Wh1z6',
        'https://t.co/izEymgg9H3',
        'https://t.co/m0f0Zkzy0Z',
        'https://t.co/kwV033RGvB',
        'https://t.co/8tjKnEM019',
        'https://t.co/cAb6t0tOqj',
        'https://t.co/YCuOez3e4e',
        'https://t.co/v9SxUOYTCy',
        'https://t.co/W6XDqLVFNk',
        'https://t.co/WZAvbohiuP',
        'https://t.co/4lU6L8FtRK',
        'https://t.co/B6FPCruJg9',
        'https://t.co/rmmwBc2XIx',
        'https://t.co/W61ynVx0b6',
        'https://t.co/7Idn9z3CPg',
        'https://t.co/K6cUVhjHLP',
        'https://t.co/sxGihbH5gL',
        'https://t.co/JE4yR6h7Gb',
        'https://t.co/N9RrsfKVBI',
        'https://t.co/ZpIWh86bBR',
        'https://t.co/FgnnsVzL5i',
        'https://t.co/MQdr2Mc7th',
        'https://t.co/0rsJCshbqt',
        'https://t.co/Z9QOlZtAal',
        'https://t.co/m91Rpgncrl',
        'https://t.co/jGuPuwWnSw',
        'https://t.co/9gVVofeykn',
        'https://t.co/CB5tYzjsX4',
        'https://t.co/uY4ZMzqrof',
        'https://t.co/fofjq9vONO',
        'https://t.co/IPYUjrnY9U',
        'https://t.co/uXZJFw9SsF',
        'https://t.co/kVJz7rQvmu',
        'https://t.co/8C4dyd0Jdn',
        'https://t.co/EcjN0NYdcI',
        'https://t.co/XPDs6mwE4L',
        'https://t.co/HADT9Cisit',
        'https://t.co/kvjANIA6ra',
        'https://t.co/bchoqU5MmS',
        'https://t.co/aGujYMpRVx',
        'https://t.co/SyMpqwB6vB',
        'https://t.co/BoXYzbcpyy',
        'https://t.co/73HOxxuOeq',
        'https://t.co/AIHG4ffWhW',
        'https://t.co/cJbWUU5W0o',
        'https://t.co/w0pQPmRTHb',
        'https://t.co/1zTkbSHiQx',
        'https://t.co/wIcMhiUC95',
        'https://t.co/2qr5rjBdhO',
        'https://t.co/s8e7R37Gkn',
        'https://t.co/nkmYxgNOum',
        'https://t.co/qJn2Zpk7A7',
        'https://t.co/zIDlgjcHLE',
        'https://t.co/5Q3mL44Odi',
        'https://t.co/opRGv5vjzI',
        'https://t.co/FL2cxmthec',
        'https://t.co/FPHp7BQZSo',
        'https://t.co/958Wabroi6',
        'https://t.co/erNIYDe2Z6',
        'https://t.co/ymJl3nmNNZ',
        'https://t.co/lKn70w9Xh2',
        'https://t.co/anfM8oIr6n',
        'https://t.co/0QS8AfE1UB',
        'https://t.co/G3tj8tMTLJ',
        'https://t.co/6MuTJ5clDW',
        'https://t.co/xsEnIUB7BH',
        'https://t.co/uj40tf8s4K',
        'https://t.co/HUvgaTfla0',
        'https://t.co/oXEmpNAuWj',
        'https://t.co/ucKqyIGCNy',
        'https://t.co/9NnHOndo4W',
        'https://t.co/fqtVTDjEQT',
        'https://t.co/gWOO2g9o3K',
        'https://t.co/oTZkVzSj1H',
        'https://t.co/kxOVHoX69d',
        'https://t.co/hQXVoWxNjB',
        'https://t.co/WOL6AgFl7k',
        'https://t.co/BEDYBJFfIZ',
        'https://t.co/PsvSxXIxXe',
        'https://t.co/2xnR8w8Iqi',
        'https://t.co/jUU1DlszPo',
        'https://t.co/g6x1nsSLsM',
        'https://t.co/JBmRDYBIVb',
        'https://t.co/w6HUFNN7wn',
        'https://t.co/Ew2UMFDJ6F',
        'https://t.co/2xQhKRGy3C',
        'https://t.co/Mj1RpKK2Xr',
        'https://t.co/hVO9Kw9KzB',
        'https://t.co/M30tS9TKEb',
        'https://t.co/dOKMh6JnN3',
        'https://t.co/EVeK31ua5l',
        'https://t.co/v4iUC1jzov',
        'https://t.co/w6GJBq77Zl',
        'https://t.co/R5vqD6HcMq',
        'https://t.co/uVERYOF3Dn',
        'https://t.co/KEXlcQYKZY',
        'https://t.co/V5lzvknRVM',
        'https://t.co/JaYx6dBGa1',
        'https://t.co/O5STxuduj9',
        'https://t.co/3x9oXoDKEu',
        'https://t.co/JBaHUxGozR',
        'https://t.co/TjvVeoNUVW',
        'https://t.co/espY1Z5eTz',
        'https://t.co/EiFn85MjHU',
        'https://t.co/3ZAnDqEzL1',
        'https://t.co/vvYlfOdsA0',
        'https://t.co/3u1fNp9M8H',
        'https://t.co/Arrs1tfEB6',
        'https://t.co/zDrqJ7zx4k',
        'https://t.co/AZke98MCpA',
        'https://t.co/qx4n5yNcvP',
        'https://t.co/l3qk97kD6R',
        'https://t.co/QiA7ERxmW6',
        'https://t.co/ExiuBTv5FW',
        'https://t.co/YYpBstiFhY',
        'https://t.co/N2w323z8Ft',
        'https://t.co/7DPU26f0sY',
        'https://t.co/fp4MA4N6XD',
        'https://t.co/uoI6LONkOS',
        'https://t.co/2MgORzms9t',
        'https://t.co/CAwD64wJVb',
        'https://t.co/mLvHnv0kMr',
        'https://t.co/c0r2FMvi7D',
        'https://t.co/TRiTANiNJz',
        'https://t.co/06ZszZhZAL',
        'https://t.co/BVy9oy7mGo',
        'https://t.co/kUSkpw5qqr',
        'https://t.co/U5alKpdFca',
        'https://t.co/LeVmQM72wr',
        'https://t.co/0Qt0jIkzYw',
        'https://t.co/NcaeMr5kfs',
        'https://t.co/ANKndqpOpg',
        'https://t.co/ALksB3QZBv',
        'https://t.co/FXGlw8I1cy',
        'https://t.co/45LBENSy16',
        'https://t.co/1LIHA2Omqj',
        'https://t.co/IJZ1N29awx',
        'https://t.co/Cl0Na1bszu',
        'https://t.co/BvWjFBR5fX',
        'https://t.co/ulvRLJUOsl',
        'https://t.co/SFLM18vPO0',
        'https://t.co/SzpbRfexl4',
        'https://t.co/sJMbnmCosi',
        'https://t.co/n1gUHb09eJ']

def get_miraliko():

    num = len(list)
    g_num = random.randint(0,num-1)

    url = list[g_num]
    num_url = [g_num+1, url]
    return num_url

def turn_10rare():
    result = []
    # 小数点第三位を切り上げて 80%, 15%, 5%
    weight = [0.8, 0.15, 0.05]
    # 9 回抽選する
    for v in range(0, 9):
        result.append(pickup_rare(weight))
    # 最後の 1 回は必ず SR が当選する
    last = "SR"
    last = "".join((last, ":", pickup_sr()))
    result.append(last)
    return result

def pickup_rare(weight):
    rarities = ["R", "SR", "UR"]
    picked_rarity = np.random.choice(rarities, p=weight)

    if picked_rarity == "UR":
        picked_rarity = "".join((picked_rarity, ":", pickup_ur()))
    if picked_rarity == "SR":
        picked_rarity = "".join((picked_rarity, ":", pickup_sr()))
    if picked_rarity == "R":
        picked_rarity = "".join((picked_rarity, ":", pickup_r()))
        
    return picked_rarity

def pickup_ur():
    ur = ["情熱的なルビースタイルえっち", "内緒のふたりごと", "ぬれぬれサファイアスタイルえっち", "手繋ぎダイヤスタイルえっち", "玩具使用トパーズスタイルえっち", "杖コツン(SEX)", "キュアップ・ラパパ！でおちんちん生やす"]
    return np.random.choice(ur)

def pickup_sr():
    sr = ["みらい誘い受け", "リコ誘い受け", "教室えっち", "お風呂えっち", "汗だくえっち","手繋ぎキス", "水着交換"]
    return np.random.choice(sr)

def pickup_r():
    r = ["手繋ぎ","交換日記","頬キス","抱きつき"]
    return np.random.choice(r)


if __name__ == '__main__':

    pic = get_miraliko()
    print "No." + str(pic[0]) + " " + pic[1]
