records = [] 

def add_income():
    category = input("please enter the type:")
    income = float(input("please enter a safey:"))
    note = input("please write the note:")

    record = {
        "type" : " income",
        "category": category,
        "income" : income,
        "note" : note
    }
    records.append(record)
    print("add inocme sucessful")

def add_expend():
    category = input("please enetr a expand")
    expand = float(input("please eneter a number"))
    note = input("please write the note")

    record = { 
        "type" : "expand",
        "category" : category,
        "expand" : expand,
        "note" : note 
    }
    records.append(record)
    print("add expand successful")


def main():
        while True:
            print()
            print('欢迎使用glenn的记账软件')
            print("1.添加收入")
            print("2.添加支出")
            print("3.查看账单")
            print("4.查看余额")
            print("5.退出")

            choice = input("选择功能")

            if choice == "1":
                add_income()
            elif choice == "2":
                add_expend()
            elif choice == "3" :
                print("you choose look bill")
            elif choice == "4":
                print("you choose look balance")
            elif choice == "5":
                print("you are take out")
                break
            else :
                print("not useful choice,please choice again")

main()

