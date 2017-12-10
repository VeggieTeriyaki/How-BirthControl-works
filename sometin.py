import csv
import random
with open('genes.csv', newline='') as csvfile:
     genes = csv.reader(csvfile, delimiter=',')
     count = 0
     gene = ""
     rand = random.randint(2,200)
     for row in genes:
     	if(row[0] != ''):
     		gene = row[0]
     	count +=1
     	if (count == rand):
     		print(gene + ' ' +row[1])