#DayDayup
dayfactor = float(input())

def dayUp(df):
    dayup = 1
    for i in range(365):
        if i % 7 in {6, 0}:
            dayup *= (1 - 0.01)
        else:
            dayup *= (1 + df)
    return dayup

while dayUp(dayfactor) < 37.78:
    dayfactor += 0.001

print("工作日努力参数是：{:.3f}".format(dayfactor))
