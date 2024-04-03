def custom_round(number: float, ndigits: int = 0) -> float:
	'''Rounds how codequest expects you to (half away from zero). `number` is the input, and `ndigits` is the number of digits to round to.'''
	number *= 10**ndigits
	result = int(number + (0.5 if number >= 0 else -0.5))
	return result / 10**ndigits

print("(Program begins)")

# INFO THAT SEND (AKA RESPOND BACK TO PROGRAM)
type_dist = (input("Do you want to enter distance as miles or kilometers (type m or k): "))
if type_dist.lower() == "m":
    type_dist = "miles"
else:
    type_dist = "kilometers"
distance = (input(f"How many {type_dist} would you like to scooter? "))



#CALULATE COST
def calulate_cost(time):
    company_A = custom_round((1 + (time * 0.15)), 3)
    if time > 5:
         company_B = custom_round((2.5 + ((time-5) * 0.12)), 3)
    else:
         company_B = 2.50
    company_C = custom_round((5 + (time * 0.06)), 3)

    cheapest = company_A
    best_company = "Company A"
    if company_B < cheapest:
        cheapest = company_B
        best_company = "Company B"
    elif company_C < cheapest:
        cheapest = company_C
        best_company = "Company C"
    return cheapest, best_company
    
#MAIN FUNCTION 
def main(distance, type_dist):
    if type_dist == "miles":
         distance = int(distance)

         #CONVERT
         original = (distance * 1.60934)
         opposite = "kilometers"
         #CALCULATE_TIME
         MPN = (15/60)
         time = distance / MPN
         #CALCULATE COST
         cost, company = calulate_cost(time)
         
    else:
         distance = float(distance)

         #CONVERT
         original = (distance/1.60934)
         opposite = "miles"
         #CALCULATE_TIME
         KPN = (24.14016/60)
         time = distance / KPN
         #CALCULATE COST
         cost, company = calulate_cost(time)
    printcost = len(str(cost))



    print(f"That is {original} {opposite}.")
    print(f"Total time in minutes: {time}.")
    if printcost == 4:
        print(f"You should use {company}. It will cost ${cost}.")
    else:
        print(f"You should use {company}. It will cost ${cost}0.")


main(distance, type_dist)

print("(Program ends)")
