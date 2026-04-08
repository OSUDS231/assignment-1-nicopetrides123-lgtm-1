distance=int(input("enter the trip distance in miles "))
average_speed=int(input("enter the average speed in miles per hour "))
fuel_efficiency=int(input("what is the fuel efficiency how many miles per gallon does your car get? "))
price_per_gallon=(float(input("what is the price per gallon of gas? ")))

drive_time=distance/average_speed
Gallons_needed= distance/fuel_efficiency
fuel_cost= price_per_gallon*Gallons_needed

print(f"'For a trip of {float(distance)} miles at an average speed of {float(average_speed)} mph, the driving time will be {float(drive_time.1f)} hours.' ")
print( )
print(f'Your car will use {float(Gallons_needed)} gallons of gas, and the total fuel cost will be ${float(fuel_cost)} ')
