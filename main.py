from datetime import datetime

#Input Earnings per Share (Past)
eps_past = {}
forward_eps = True

while forward_eps == True:
    eps_number = input("Input the EPS from a Past Year: ")
    eps_year = input("Input the Year from the EPS: ")
    update_eps_past = {eps_year:eps_number}
    eps_past.update(update_eps_past)

    while True:
        add_more_eps = input("Want to input more Past EPS Data? (y/n): ")

        if add_more_eps == "n" or add_more_eps == "N":
            forward_eps = False
            break
        elif add_more_eps == "y" or add_more_eps == "Y":
            forward_eps = True
            break
        else:
            print("Wrong Answer... Try again!")

#Quick Test of Dictionary
print(eps_past)

#Calculate Average Interest Earnings per Share (Past to Present)
interest_past = ()




#Input Assumption of the Future Interest

#Calculate EPS in 10 Years
today = datetime.now().year
