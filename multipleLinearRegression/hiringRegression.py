# price = m1 * area + m2 * bedrooms + m3 * age + b

import pandas as pd
from sklearn import linear_model
from word2number import w2n
from sklearn.linear_model import LinearRegression
import math as m


def manage_data():
    df.experience = df.experience.apply(lambda x: w2n.word_to_num(x) if isinstance(x, str) else x)
    df.experience = df.experience.fillna(0)
    average = m.floor(df.test_score.median())
    df.test_score = df.test_score.fillna(average)


def regression(df):
    reg = linear_model.LinearRegression()
    reg.fit(df[['experience','test_score','interview_score']],df.salary)
    return reg


def main(reg):
    while True:
        experience = float(input('Experience: '))
        test_score = float(input('Test score: '))
        interview_score = float(input('Interview score: '))
        predicted_salary = reg.predict([[experience,test_score,interview_score]])[0]
        print(f"The recommended salary is: {round(predicted_salary,2)} $ per year")
        input_user = input("Press zero to leave")
        if input_user == '0':
            break


df = pd.read_csv('hiring.csv')
manage_data()
reg = regression(df)
main(reg)



