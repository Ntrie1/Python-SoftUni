deposit = float(input())
timeDue = int(input())
annual_Interest = float(input())

accrued_intrest = deposit * (annual_Interest / 100)
monthly_intrest = accrued_intrest / 12
finalAmount = deposit + (timeDue * monthly_intrest)

print(finalAmount)