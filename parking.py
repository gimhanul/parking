from pandas import DataFrame
import csv

data = {}
name = []
we = []
gyeong = []
cars = []

with open('data.csv', 'r', encoding='UTF8') as f:
    reader = csv.reader(f)
    
    for row in reader:
        if row[0][-5:] != '(주거지)' and row[3] != '경도': #(주거지)
            name.append(row[0])
            cars.append((int)(row[1]))
            we.append((float)(row[2]))
            gyeong.append((float)(row[3]))

data['위도'] = we
data['경도'] = gyeong
data['이름'] = name
data['주차가능대수'] = cars

print(data)
