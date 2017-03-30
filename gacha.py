#coding: utf-8
import random
import numpy as np

#空の短縮URL用リスト
miraliko_list = []

f = open('picture_list.txt', 'r')
#1行ずつ格納
for line in f:
    miraliko_list.append(line)

f.close()

def get_miraliko():

    #リストの総数から、画像のインデックス番号をランダムで選択
    num = len(miraliko_list)
    pic_index = random.randint(0,num-1)

    url = miraliko_list[pic_index]
    num_and_url = [str(pic_index+1), url]
    #画像番号と短縮URLのセットをリストで返す
    return num_and_url

'''
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
'''

if __name__ == '__main__':

    pic = get_miraliko()
    print "No." + pic[0] + " " + pic[1]
