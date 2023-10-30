from datetime import datetime
from collections import defaultdict


def get_birthdays_per_week(users):
    happy_days = defaultdict(list)
    current_day = datetime(year=2023, month=10, day=28)
    current_day = datetime.date(current_day)
    for user in users:
        user_Bday = user["birthday"]
        user_Bday = datetime.date(user_Bday)
        birthday_this_year = user_Bday.replace(year=current_day.year)

        if birthday_this_year < current_day:
            birthday_this_year = birthday_this_year.replace(
                year=current_day.year+1)
        delta_days = (birthday_this_year - current_day).days

        if delta_days < 7:
            day_of_the_week = birthday_this_year.strftime("%A")
            current_week_day = current_day.strftime("%A")
            if day_of_the_week == "Saturday" or day_of_the_week == "Sunday":
                if (current_week_day == "Sunday" or current_week_day == "Monday") and birthday_this_year > current_day:
                    continue

                happy_days["Monday"].append(user["name"])
                continue
            happy_days[day_of_the_week].append(user["name"])

    if len(happy_days) == 0:
        return "There is no birthdays in you contacts book."
    else:
        show_bd(happy_days)


def show_bd(happy_days):
    result = list()
    for day, names in happy_days.items():
        weekday_and_names = str()
        weekday_and_names += day + ": "
        for name in names:
            weekday_and_names += name + ", " if name != names[-1] else name
        result.append(weekday_and_names)
    print("\n".join(result))


get_birthdays_per_week([
    {"name": "Bill", "birthday": datetime(1955, 10, 24)}])


# , {"name": "Gates", "birthday": datetime(1955, 10, 25)}, {"name": "Bill Gates", "birthday": datetime(1955, 11, 14)}, {"name": "Lara Gray", "birthday": datetime(1955, 11, 9)}, {"name": "Nick Ross", "birthday": datetime(1956, 11, 5)}, {"name": "Tedd", "birthday": datetime(1956, 11, 6)}, {"name": "Ron", "birthday": datetime(1956, 11, 7)}
