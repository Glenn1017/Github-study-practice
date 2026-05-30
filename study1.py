import csv

content = input("what are you learn today?")
time = input("how many time are you studying? ")

with open ("study.log.csv","a") as file:
    writer = csv.writer(file)
    writer.writerow([content,time])
    
    
