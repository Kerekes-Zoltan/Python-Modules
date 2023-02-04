import random
import datetime

print("Generate a random integer between 0 and 6: ", random.randrange(5))
print("\nGenerate a random integer between 5 and 10, excluding 10: ", random.randrange(start=5, stop=10))
print("\nGenerate a random integer between 0 and 10, with a step of 3: ", random.randrange(start=0, stop=10, step=3))

date1 = datetime.date(2019, 2, 1)
date2 = datetime.date(2019, 3, 1)

time_between_dates = date2 - date1
days_between_dates = time_between_dates.days
random_number_days = random.randrange(days_between_dates)
random_date = date1 + datetime.timedelta(days=random_number_days)
print("\nRandom date between two dates: ", random_date)