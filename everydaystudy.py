from datetime import date,timedelta
today = date.today()
print("today is :", today)
content = input("what are you learning today?")
print("today you studied coentent is:",content)
with open("study_log.txt","a") as file:
    file.write(str(today) + "-" + content + "\n")

date = []
with open("study_log.txt","r") as file:
    for line in file:
        check_date = line.split("-")[0]
        date.append(check_date)

streak  = 0 
day = today 

while str(day) in date:
    streak += 1 
    day = day - timedelta(day =1 )


print("saved!!")
print("you have checked in", streak, "days in a row")
