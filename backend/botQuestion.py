#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu Jul  5 11:11:47 2018

@author: jeanc
"""

from services.BotService import Bot
import pandas as pd
import datetime
from sqlalchemy import create_engine
import time
import numpy as np

bot = Bot()

Question = pd.read_csv("Exercises Questions.csv")
Question = Question.fillna("Question")

start = datetime.datetime(2018, 8, 20)

#engine = create_engine("mysql://jeanchen:LARCdata9696@10.0.106.72:3307/jeanchen")
#sql_bot = 'SELECT * FROM avatar where is_bot is null'
#botList = pd.read_sql(sql=sql_bot,con=engine)

while True:
    print datetime.datetime.now()
    daydiff = (datetime.datetime.today()-start).days
    Ques = Question[Question['Day']-1 == daydiff].to_dict("records")
    #Ques = Question.to_dict("records")

    for q in Ques:
	for i in range(5):
	    post = {}
	    post['subject'] = q['Exercise']
	    post['question'] = q['Question ']
	    print post['question']
	    post['userId'] = i+1
	    bot.newPost(post)
	    print post['question']
            
    time.sleep(86400)
