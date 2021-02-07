seconds = int(input("Enter the number of seconds:"))
if seconds >= 86400:
    days = seconds/86400
    
elif seconds >= 3600:
    hours =seconds/3600
elif seconds >= 60:
    minutes = seconds/60