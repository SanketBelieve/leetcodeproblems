import datetime
def dayOfTheWeek(d: int, m: int, y: int) -> str:
    return datetime.datetime(y,m,d).strftime("%A")

print(dayOfTheWeek(31,8,2019))