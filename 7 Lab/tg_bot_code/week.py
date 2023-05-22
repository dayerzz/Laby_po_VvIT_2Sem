import datetime


def curr_week():
    today = datetime.datetime.today()
    week_num = today.isocalendar()[1]
    if week_num % 2 == 0:
        return "ЧЁТНАЯ"
    else:
        return "НЕЧЁТНАЯ"

def curr_week_for_bd(x):
    if x == 1:
        if curr_week() == "НЕЧЁТНАЯ":
            return 1
        else:
            return 2
    if curr_week() == "НЕЧЁТНАЯ":
        return 2
    else:
        return 1