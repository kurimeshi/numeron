#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Aug 22 01:41:20 2020

@author: kurimeshi
"""
import random
import sys


class Preparation: 
    def __init__(self):
        preparation=0
        while preparation!=1:
            a1=random.randint(0,9)
            a2=random.randint(0,9)
            a3=random.randint(0,9)
            self.a1=str(a1)
            self.a2=str(a2)
            self.a3=str(a3)
            preparation=0
            if a1!=a2:
                if a1!=a3:
                    if a2!=a3:
                        preparation+=1
    
    
class Check:
    def __init__(self,A1,A2,A3,Q1,Q2,Q3):
        self.a1=A1
        self.a2=A2
        self.a3=A3
        self.q1=str(Q1)
        self.q2=str(Q2)
        self.q3=str(Q3)
        self.eat=0
        self.bite=0
        la=[self.a1,self.a2,self.a3]
        lq=[self.q1,self.q2,self.q3]
        for (q,a) in zip(lq,la):
            if q==a:
                self.bite+=1
                self.eat-=1
        for (Q) in lq:
            for (A) in la:
                if Q==A:
                    self.eat+=1
        
    def check(self):
        print('{}eat{}bite'.format(self.eat,self.bite))
                    
                
class Result:
    def __init__(self,t,n):
        self.times=t
        self.name=n
        

class Question:
    def __init__(self):
        self.q1=input('_?? 入力してください．>>')
        self.q2=input('{}_? 入力してください．>>'.format(self.q1))
        self.q3=input('{}{}_ 入力してください．>>'.format(self.q1,self.q2))
        
    def question(self):
        print('あなたの質問は{}{}{}です．'.format(self.q1, self.q2,self.q3))
        self.select=input('よろしければy,変更したい場合はnと入力してください．>>')
        
    def displayanswer(self,a):
        if self.select=='displayanswer':
            print(a)
        

class No:
    
    def __init__(self):
        self.l = []
    
    def record(self,t):
        self.name=input('名前を入力してください． >>')
        self.rec=[t,self.name]
        
    def number(self):
        self.l.append(self.rec)
        self.l.sort()
    
    def displaynumber (self):
        n=1
        for i in self.l:
            print('{}位:{} 質問回数:{}回'.format(n,i[1],i[0]))
            n+=1
    
                  
class Game:
    def play_game():
        n=No()
        print('ヌメロン ')
        tell=input('ゲームの説明は必要ですか? y/n>>')
        
        if tell=='y':
            print('このゲームはコンピュータに質問をすることでコンピュータが選択した0~9の数字を使った三桁の数を当てるゲームです．')
            print('コンピュータはプレイヤーが入力した三桁の数に関して，数と桁の場所があっている数がn個あれば n bite，')
            print('桁は合っていないがコンピュータの選択した数の中に含まれている数がm個あれば　m eat と　回答します．')
            print('プレイヤーがコンピュータの選択した数を入力したらゲームが終了します．')
            print('（数字の重複はありません．）')
            print('ゲームの説明は以上です．')  
        question=input('ゲームを開始しますか? y/n>>')
            
        while question=='y':
                ans=Preparation()
                a1=ans.a1
                a2=ans.a2
                a3=ans.a3
                answer=a1+a2+a3
                time=0
                q1=0
                q2=0
                q3=0
                
                while q1+q2+q3!=answer:
                    select='n'
                    
                    while select=='n':
                        q=Question()
                        q.question()
                        select=q.select
                        q1=q.q1
                        q2=q.q2
                        q3=q.q3
                        q.displayanswer(answer)
                    c=Check(a1,a2,a3,q1,q2,q3)
                    c.check()
                    time+=1
                    
                else:
                    print('正解です．正解するまでの質問回数は{}回でした．'.format(time))
                    rec=input('記録を保存しますか? y/n>>')
                    if rec=='y':
                        n.record(time)
                        n.number()
                        n.displaynumber()
                    
                question=input('もう一度挑戦しますか? y/n>>')
                
        else:
                sys.exit()
                
                    

                    
                    
                
                
                
                
                
        

   




