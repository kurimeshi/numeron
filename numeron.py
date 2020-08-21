# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import random
import sys
print('ヌメロン')
tell = input('ゲームの説明は必要ですか？ y/n>>')
if tell == 'y' :
    print('このゲームはコンピュータに質問をすることでコンピュータが選択した0~9の数字を使った三桁の数を当てるゲームです．')
    print('コンピュータはプレイヤーが入力した三桁の数に関して，数と桁の場所があっている数がn個あれば n bite，')
    print('桁は合っていないがコンピュータの選択した数の中に含まれている数がm個あれば　m eat と　回答します．')
    print('プレイヤーがコンピュータの選択した数を入力したらゲームが終了します．')
    print('（数字の重複はありません．）')
    print('ゲームの説明は以上です．')
    tell = 'n'
preparation = 0
#重複が起こらないように重複していない三桁の数字ができるまで数を変更します．    
while preparation != 3 :    
    a1 = random.randint(0,9)
    a2 = random.randint(0,9)
    a3 = random.randint(0,9)
    a1 = str(a1)
    a2 = str(a2)
    a3 = str(a3)     
    preparation = 0
    if a1 != a2 :
        preparation = preparation + 1
        if a1 != a3 :
          preparation = preparation + 1
          if a2 != a3 :
            preparation = preparation + 1
else :                               
    question = input('ゲームを開始しますか？　y/n>>')
    if question == 'y':
        time = 0
        answer = a1 + a2 + a3
        q1 = 0
        q2 = 0
        q3 = 0
        eat = 0
        bite = 0
#プレーヤーの回答が答えと一致するまで繰り返します．
        while q1 + q2 + q3 != answer :
            select = 'n'
            while select == 'n' :
                q1 = input('_?? 入力してください．>>')
                q2 = input(q1 + '_? 入力してください．>>')
                q3 = input(q1 + q2 +'_ 入力してください．>>')
                print('あなたの質問は' + str(q1) + str(q2) + str(q3) + 'です．')
                select = input('よろしければy，変更したい場合はnと入力してください．>>')
#nを選択すると質問を変更できます．
            if select == 'y' :
                eat = 0
                bite = 0
                la = [a1,a2,a3]
                lq = [q1,q2,q3]
                for (q,a) in zip(lq,la) :
                    if q == a:
                        bite = bite + 1
                        eat = eat - 1
                for(Q) in lq:
                    for(A) in la:
                        if Q == A:
                            eat = eat + 1
 #きちんと動くかどうかの確認だけをしたい時にこれを入力する事で答えが表示されます．
            if select == 'displayanswer':
                print(answer)
            print(str(eat) + 'eat' + str(bite) + 'bite')
            time = time + 1
        else :
            print('正解です．正解するまでの質問回数は' + str(time) + '回でした．')
    if question == 'n' :
        sys.exit()
        
        
        
        