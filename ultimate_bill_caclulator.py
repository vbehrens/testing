Bill_amount=int(raw_input ("how much was your total bill not including tip?"))
Dine_alone =raw_input("Did you dine alone? answer Y or N")
tip_amount = 0
#print Dine_alone
if Dine_alone == 'Y':
	tip_18_okay = raw_input("Is 18 percent tip ok? Y or N ")
	if tip_18_ok == 'Y':
		tip_amount= bill_amount * .18
	else: raw_input("How much do you want to")
else: amount_ppl=raw_input("How many people were at dinner?")
# amount_people= int(raw_input("how many people were at dinner? Answer Y or N "))





