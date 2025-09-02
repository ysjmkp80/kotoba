# quiz.py
# -*- coding: utf-8 -*-
# 単純な三択クイズ

# 問題と答えの一式
qa = ( "このプログラミング言語は何でしょう？","PHP","Python","Ruby", 2 )

# 出題
print('\n問題：' + qa[0] + '\n')

# 答えを入力
x = input('1. ' + qa[1] + ', 2. ' + qa[2] + ', 3. ' + qa[3] + ' > ')
x = int(x)

# 正解の番号
y = int(qa[4])

# 答え合わせ
if x == y :
    print('\n正解っす。\n')
else :
    print('\nちげーよ！\n')

