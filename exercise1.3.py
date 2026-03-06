#input
distance_kilometers = 10
time_minutes = 42
time_seconds = 42
#transformation
distance_kilometers_to_miles = 10 / 1.61
time_minutes_to_seconds = time_seconds + (42 * 60)
average_pace = time_minutes_to_seconds / distance_kilometers_to_miles
#output
print(average_pace)

#transformations2
average_pace2 = (time_minutes / distance_kilometers_to_miles) + average_pace
print(average_pace2)

#transformations3
time_seconds_to_minutes = 42 / 60
time_minutes_to_hours = time_seconds_to_minutes + (42 / 3600)
speed_miles_per_hour = distance_kilometers_to_miles / time_minutes_to_hours

print(speed_miles_per_hour)
