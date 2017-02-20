#coding: utf-8
import random
import numpy as np

list = [['UR01', 'https://t.co/2uTyEJvHbT'],
        ['UR02', 'https://t.co/QBuG76TNKw'],
        ['SR01', 'https://t.co/mWGPNr8TQF'],
        ['SR02', 'https://t.co/xT2Z9kPGTQ'],
        ['R01',  'https://t.co/XTuuOFvP94'],
        ['R02',  'https://t.co/Z6wpZzf1yo']]

def get_miraliko():

    weight = [0.01, 0.01, 0.2, 0.2, 0.25, 0.25]
    num = len(list)
    g_num = random.randint(0,num-1)

    list1 = list[g_num]
    return list1

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
