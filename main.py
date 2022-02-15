import random
#Part A
weeks = 16
classes = 5
tuition = 6000
cost_per_week = ((tuition / classes) / weeks)
print("Cost per week:", cost_per_week)
classes_per_week = 3
cost_per_class =  (cost_per_week/classes_per_week)
print("Cost per class:",cost_per_class)
print("message - how was your weekend?:))")
print(weeks,type(weeks))
print(classes,type(classes))
print(tuition,type(tuition))
print(cost_per_week,type(cost_per_week))
print(classes_per_week, type(classes_per_week))
print(cost_per_class, type(cost_per_class))



#Part B
#list part B
print("Part B")
wow = ['hello', 20, 30, 40, 7.5]
print (wow)
print(random.choice(wow))
