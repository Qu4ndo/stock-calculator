def input_eps():
    #Input Earnings per Share (Past)
    eps_past = []

    while True:
        input_counter = len(eps_past) + 1
        eps_number = input("Input the EPS from the " + str(input_counter) + " Year: ")

        if eps_number == "n" or eps_number == "N":
            break
        else:
            eps_past.append(float(eps_number))

    len_eps_past = len(eps_past)

    return eps_past, len_eps_past

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
        av_interest = sum(eps_calc)
        av_interest = av_interest / calc_counter
        av_interest = round(av_interest, 2)
    else:
        av_interest = round(eps_calc[0], 2)

    return av_interest

def input_assumption():
    #Input Assumption of the Future Interest
    interest_future = float(input("Input your Interest Expectation (%) for EPS in the Future: "))
    txt_interest_future = interest_future
    interest_future = interest_future / 100
    interest_future += 1
    last_eps = float(input("Input your last EPS Data (from the Present): "))

    return interest_future, last_eps, txt_interest_future

def eps_future(last_eps):
    #Calculate EPS in 10 Years
    future_counter = 11
    future_eps = last_eps

    while future_counter > 0:
        future_eps = future_eps * interest_future
        future_counter -= 1

    return future_eps

def price_future(future_eps):
    #Input P/E-Ratio in 10 Years
    per_future = float(input("Input your P/E-Ratio Expectation for the Future: "))

    #Calculate Price per Share in 10 Years = EPS in 10 Years x KGV in 10 Years
    pps_future = future_eps * per_future

    return pps_future, per_future

def price_now(pps_future):
    #Calculate Interest per Year (Default = 12%) --> 1,12^10 = Factor 10 Years
    factor = 3.1058482083
    pps_now = pps_future / factor

    return pps_now

def output_txt(eps_past, eps_rounded, av_interest, txt_interest_future, last_eps, future_eps, pps_future, pps_now):
    write_txt = input("Save this to file? (y/n): ")
    if write_txt == "y" or write_txt == "Y":
        name = input("Input filename: ")
        filename = name + ".txt"
        text_file = open(filename, "w")
        text_file.write("                ######## " + str(name) + " ########\n\n\n")
        text_file.write("Input: \n\n")
        text_file.write("Past EPS Data: " + str(eps_past) + "\n\n")
        text_file.write("Latest EPS Data: " + str(last_eps) + " €/$ \n")
        text_file.write("Future Interest Expectation (EPS): " + str(round(txt_interest_future, 2)) + "%\n")
        text_file.write("P/E-Ratio Expectation: " + str(per_future) + "\n\n")
        text_file.write("#####################################################################\n\n")
        text_file.write("Output: \n\n")
        text_file.write("Interest Past EPS Data (%): " + str(eps_rounded) + "\n")
        text_file.write("Average Interest Past EPS Data: " + str(round(av_interest, 2)) + "%\n\n")
        text_file.write("Future EPS (10 Years): " + str(round(future_eps, 2)) + " €/$\n")
        text_file.write("Price per Share (10 Years): " + str(round(pps_future, 2)) + " €/$\n")
        text_file.write("Fair Price per Share (Present): " + str(round(pps_now, 2)) + " €/$\n\n")
        text_file.write("#####################################################################\n")
        text_file.close()

if __name__ == "__main__":
    print("Warning! Input the Data in correct order (Past to Present)!")
    print("Info: Stop the input with \"n\" or \"N\"!")
    print("#####################################################################")
    eps_past, len_eps_past = input_eps()
    if len_eps_past > 1:
        eps_calc = calculate_interest(eps_past)
        av_interest = average_interest(eps_past, eps_calc)
        print("Your Average Interest of this Stock was: " + str(av_interest) + "%")
    print("#####################################################################")
    interest_future, last_eps, txt_interest_future = input_assumption()
    future_eps = eps_future(last_eps)
    print("Your Future EPS (10 Years) is: " + str(round(future_eps, 2)) + " €/$")
    print("#####################################################################")
    pps_future, per_future = price_future(future_eps)
    print("Your Price per Share (10 Years) is: " + str(round(pps_future, 2)) + " €/$")
    print("#####################################################################")
    pps_now = price_now(pps_future)
    print("Your Fair Price per Share (Present) is: " + str(round(pps_now, 2)) + " €/$")
    print("#####################################################################")
    eps_rounded = []
    for i in eps_calc:
        eps_rounded.append(round(i, 2))
    output_txt(eps_past, eps_rounded, av_interest, txt_interest_future, last_eps, future_eps, pps_future, pps_now)
