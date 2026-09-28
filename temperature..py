city = input("Enter your city names ")
temp = float(input("Enter today's temperature"))

if temp > 35:
    print("It will be hot today")

if temp > 25:
    print("Great day to go outside")
else:
    print ("Grab a jacket before you go out.")

if temp > 35:
    print("Weather: Scorching hot")
elif temp > 25:
    print("Weather: Warm and Sunny")
elif temp > 15:
    print("Weather: Cool and Breezy")
else:
    print("Weather: Cold")

import datetime
import calendar
now = datetime.datetime.now()
print("City:", city)
print("Time now", now)

print(calendar.calendar(now.year))

