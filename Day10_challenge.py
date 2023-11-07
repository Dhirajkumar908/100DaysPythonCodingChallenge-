myBill = float(input("What was the bill?: "))
numberOfPeople = int(input("How many people?: "))
tipPercentage = int(
    input("What percentage tip to be added ? it can be 15%, 18%, 20% :"))
if tipPercentage == 15:
    tipAmount = myBill * 0.15
    totalBill = myBill + tipAmount
    answer = totalBill / numberOfPeople
    answer = round(answer, 2)
    print("You all owe", answer)

elif tipPercentage == 18:
    tipAmount = myBill * 0.18
    totalBill = myBill + tipAmount
    answer = totalBill / numberOfPeople
    answer = round(answer, 2)
    print("You all owe", answer)

elif tipPercentage == 20:
    tipAmount = myBill * 0.20
    totalBill = myBill + tipAmount
    answer = totalBill / numberOfPeople
    answer = round(answer, 2)
    print("You all owe", answer)
else:
    answer = myBill / numberOfPeople
    answer = round(answer, 2)
    print("You all owe", answer)
