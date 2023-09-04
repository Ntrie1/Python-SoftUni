from math import floor

pages =  int(input())
pages_per_hour = int(input())
required_days = int(input())


timeRequired = pages / pages_per_hour
neededHours = timeRequired / required_days

print(floor(neededHours))