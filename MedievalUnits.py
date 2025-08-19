import math

print('How many talents?')
talents = float(input())
print('How many pounds?')
pounds = float(input())
print('How many lots?')
lots = float(input())

pounds = pounds + (talents * 20)
lots = lots + (pounds * 32)

grams = lots * 13.3

print(grams)

kilograms = math.floor(grams / 1000)
grams = grams - (kilograms * 1000)
grams = round(grams,3)

print('The weight in modern units is ' + str(kilograms) + ' kilograms and ' + str(grams) + ' grams.')