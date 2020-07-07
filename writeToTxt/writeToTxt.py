import csv, os
file = open('E:\\Dokumente\\Dataset\\newsqa-data-v1.csv')
questions = open('E:\\Dokumente\\Dataset\\Questions.txt', 'w')
toRead = csv.reader(file)
try:
    data = list(toRead)
except:    
    data = list(toRead)
for i in range(len(data)):
    print(data[i][1])
    DataToWrite = str(data[i][1]) + '\n'
    questions.write(DataToWrite)
questions.close()