#Input Earnings per Share (Past)
eps_past = {}
forward_eps = True

while forward_eps == True:
    eps_number = input("Input the EPS for a Past Year: ")
    eps_year = input("Input the Year from the EPS: ")
    update_eps_past = {eps_year:eps_number}
    eps_past.update(update_eps_past)

    add_more_eps = input("Want to input more Past EPS Data? (y/n): ")

    if add_more_eps == "no":
        forward_eps = False

print(eps_past)
