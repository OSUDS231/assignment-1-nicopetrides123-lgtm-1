time= int(input("Please enter a number of seconds to convert into hours, minutes, seconds:"))
hours=time//3600
minutes=time%3600//60
seconds=time%60
print(f'{hours} hours  {minutes} minutes {seconds} seconds')
