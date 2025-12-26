#yours chaiwala
order=input('''--------------food menue---------------
            1-tea   : Rs 30
            2-cofee : Rs 50
            3-cold drink : Rs 80
            Which one do you prefer please write the name : ''')
if order=="tea":
    suger=input("do you want some extra suger : ")
    if suger =="yes":
        print("your bill : Rs 40")
    else:
        print("your bill : Rs 30")
elif order =="cofee":
    suger1=input("do you want some extra suger : ")
    if suger1 =="yes":
        print("your bill : Rs 60")
    else:
        print("your bill : Rs 50")
elif order =="cold drink":
        print("your bill : Rs 60")
    
