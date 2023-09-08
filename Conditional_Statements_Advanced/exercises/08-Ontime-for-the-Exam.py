exam_hour = int(input())
exam_minute = int(input())
arrival_hour = int(input())
arrival_minute = int(input())

exam_time = exam_hour * 60 + exam_minute
arrival_time = arrival_hour * 60 + arrival_minute

time_difference = arrival_time - exam_time

if time_difference > 0:
    print('Late')
elif -30 <= time_difference <= 0:
    print('On time')
else:
    print('Early')

result = abs(exam_time - arrival_time)
if exam_time - arrival_time > 0:
    if result < 60:
        print(f"{result} minutes before the start")
    else:
        hours = result // 60
        minutes = result % 60
        if minutes < 10:
            print(f"{hours}:{minutes:02d} hours before the start")
        else:

            print(f"{hours}:{minutes} hours before the start")

elif arrival_time - exam_time > 0:
    if result < 60:

        print(f"{result} minutes after the start")
    else:
        hours = result // 60
        minutes = result % 60
        if minutes < 10:

            print(f"{hours}:{minutes:02d} hours after the start")


        else:

            print(f"{hours}:{minutes} hours after the start")

