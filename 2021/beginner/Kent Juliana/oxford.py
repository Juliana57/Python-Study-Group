current_tuition = 8000
new_tuition = []

for i in range (0,10):
    projected_tution = current_tuition + current_tuition+2.2/100
    new_tuition.append(projected_tution)

total_sum = sum(new_tuition)
print("The projected sum in the next 10 years is $",total_sum)

