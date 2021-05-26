exam_hour = int(input())
exam_minutes = int(input())
arrive_hour = int(input())
arrive_minutes = int(input())
exam_time = exam_hour * 60 + exam_minutes
arrive_time = arrive_hour * 60 + arrive_minutes
if arrive_time > exam_time:
    print("Late")
elif exam_time - 30 <= arrive_time <= exam_time:
    print("On time")
elif exam_time - 30 > arrive_time:
    print("Early")
if exam_time - 60 < arrive_time < exam_time:
    print(f"{exam_time - arrive_time} minutes before the start")
elif exam_time - 60 >= arrive_time:
    hours = (exam_time - arrive_time) // 60
    minutes = (exam_time - arrive_time) % 60
    print(f"{hours}:{minutes:0>2d} hours before the start")
elif exam_time < arrive_time < exam_time + 60:
    print(f"{arrive_time - exam_time} minutes after the start")
elif arrive_time >= exam_time + 60:
    hours = (arrive_time - exam_time) // 60
    minutes = (arrive_time - exam_time) % 60
    print(f"{hours}:{minutes:0>2d} hours after the start")