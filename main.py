def input_eps():
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

    return eps_past

def calculate_interest(eps_past):
    #Calculate Interest Earnings per Share (Past to Present)
    x = 0
    y = 1
    eps_calc = []
    calc_counter = len(eps_past)

    while calc_counter > 1:
        interest = eps_past[y] / eps_past[x]
        interest = (interest - 1) * 100
        eps_calc.append(interest)
        x += 1
        y += 1
        calc_counter -= 1

    return eps_calc

def average_interest(eps_past, eps_calc):
    #Calculate Average Interest per Share in the Past
    x = 0
    y = 1
    calc_counter = len(eps_past) - 1

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
    print("#####################################################################")


def input_assumption():
    #Input Assumption of the Future Interest
    interest_future = float(input("Input your Interest Expectation (%) for EPS in the Future: "))
    interest_future = interest_future / 100
    interest_future += 1
    last_eps = float(input("Input your last EPS Data (from the Present): "))

    return interest_future, last_eps

def eps_future(last_eps):
    #Calculate EPS in 10 Years
    future_counter = 11
    future_eps = last_eps

    while future_counter > 0:
        future_eps = future_eps * interest_future
        future_counter -= 1

    print("Your Future EPS (10 Years) is: " + str(round(future_eps, 2)) + " €/$")
    print("#####################################################################")

    return future_eps

def price_future():
    #Input KGV in 10 Years
    kgv_future = float(input("Input your KGV Expectation for the Future: "))

    #Calculate Price per Share in 10 Years = EPS in 10 Years x KGV in 10 Years
    pps_future = future_eps * kgv_future
    print("Your Price per Share (10 Years) is: " + str(round(pps_future, 2)) + " €/$")
    print("#####################################################################")

def price_now():
    #Calculate Interest per Year (Default = 12%) --> 1,12^10 = Factor 10 Years
    factor = 3.1058482083
    pps_now = pps_future / factor

    print("Your Fair Price per Share (Present) is: " + str(round(pps_now, 2)) + " €/$")

if __name__ == "__main__":
    eps_past = input_eps()
    eps_calc = calculate_interest(eps_past)
    average_interest(eps_past, eps_calc)
    interest_future, last_eps = input_assumption()
    eps_future(last_eps)
    exit()
    price_future()
    price_now()
