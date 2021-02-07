my_list = []
n = int(input("how many times have you run around a race track:"))
for i in range(0, n):
    lap_time = float(input("Enter Lap Time:"))
    my_list.append(lap_time)
    
maximum = max(my_list)
minimum = min(my_list)
average = (sum(my_list))/n

print("The fastest lap time is", maximum,"seconds")
print("The slowest lap time is", minimum,"seconds")
print("The average lap time is", average,"seconds")


