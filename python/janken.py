# janken.py
# -*- coding: utf-8 -*-
# 参照: https://www.amazon.co.jp/ゲーム作りで学ぶPython―作って動かして遊びながら学ぶプログラミング-日向-俊二/dp/4877834575
# 参照: Pythonでじゃんけんポイっ　初心者向け(回答と解説） https://qiita.com/sandream/items/01374069f447b7748eba

import random
random.seed()

def game() :
    # 手を数値で入力する
    x = input('あなたの手は？ (グー=1，チョキ=2，パー=3，終わり=0) > ')
    x = int(x)

    # 入力ミスの処理
    if x<0 or x>3 :
        print('0〜3の整数を入力してください')
        return x

    # 終わりの場合
    if x == 0 :
        return 0

    # 手の候補
    dic = { 1 : "グー", 2 : "チョキ", 3 : "パー"}

    # あなたの手を表示
    print('あなたの手は' + dic[x] + 'です。')

    # コンピュータの手を表示
    y = random.randint(1, 3)
    print('私の手は' + dic[y] + 'です。')

    # 勝敗の判定
    if y == x :
        print('引き分け。')

    elif y - x == 1 or x - y == 2 :
        print('あなたの勝ち！')

    else :
        print('あなたの負け。')

    return x

# 繰り返し
fLoop = 99

while fLoop != 0 :
    fLoop = game()

