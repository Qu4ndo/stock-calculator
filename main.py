#Input Earnings per Share (Past)
eps_past = []
forward_eps = True
input_counter = 1
print("Warning! Input the Data in correct order (Past to Present)!")

while forward_eps == True:
    eps_number = input("Input the EPS from the " + str(input_counter) + " Year: ")
    eps_past.append(float(eps_number))

    if input_counter < 2:
        input_counter += 1
    else:
        while True:
            add_more_eps = input("Want to input more Past EPS Data? (y/n): ")

            if add_more_eps == "n" or add_more_eps == "N":
                forward_eps = False
                break
            elif add_more_eps == "y" or add_more_eps == "Y":
                forward_eps = True
                input_counter += 1
                break
            else:
                print("Wrong Answer... Try again!")

#Calculate Interest Earnings per Share (Past to Present)
x = 0
y = 1
eps_calc = []
calc_counter = input_counter

while calc_counter > 1:
    interest = eps_past[y] / eps_past[x]
    interest = (interest - 1) * 100
    eps_calc.append(interest)
    x += 1
    y += 1
    calc_counter -= 1

#Calculate Average Interest per Share in the Past
x = 0
y = 1
calc_counter = input_counter - 1

if calc_counter > 1:
    while calc_counter > 1:
        av_interest = eps_calc[x] + eps_calc[y]
        x += 1
        y += 1
        calc_counter -= 1

    input_counter -= 1
    av_interest = av_interest / input_counter
    av_interest = round(av_interest, 2)
else:
    av_interest = round(eps_calc[0], 2)

#Output Average Interest per Share in the Past
print("Your Average Interest of this Stock was: " + str(av_interest) + "%")

#Input Assumption of the Future Interest

#Calculate EPS in 10 Years
