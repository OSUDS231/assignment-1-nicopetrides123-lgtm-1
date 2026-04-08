distance=int(input("enter the trip distance in miles "))
speed=int(input("enter the average trip speed in miles per hour "))
mpg=int(input("how many miles per gallon does your car get? "))
gas=(float(input("what is the price of gas? ")))

drive_time=distance/speed
Gallons_needed= distance/mpg
fuel_cost= gas*Gallons_needed

print(f"for a trip of {float(distance)} miles and an average speed of {speed} miles per hour, the driving time will be {drive_time} hours ")
print( )
print(f'your car will use {Gallons_needed} gallons of gas, and the total fuel cost will be ${fuel_cost} ')
