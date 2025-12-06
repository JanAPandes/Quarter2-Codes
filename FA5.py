#Quarter 2 FA 5 - Activity 3: Travel Itinerary Planner - Manipulating Arrays

'''

GRASPS Design:

Goal: Practice updating and modifying elements within an array.

Role: Developer of a simple travel app.

Audience: A user planning a vacation itinerary.

Situation: The user inputs five travel destinations. Later, they want to update the second and fifth destinations.

Product: A program that stores travel destinations in an array, allows updates to specific elements, and displays the updated list.


Standards:

Proper use of array indices to update values.

Program accurately reflects changes and displays the final list.

Good readability and user interaction.

'''

import array
arr = []

print("Please enter your 5 travel destinations:")


count = 0
for i in range(1,6):
    count += 1
    location = str(input(f"Destination {count}: "))
    arr.append(location)

count = 0
print('''
Original Travel Itinerary:''')
for s in arr:
    count += 1
    print(f"{count}. {s}")

print('''
Let's update your 2nd and 5th destinations.''')

new_location2 = str(input("Enter a new destination for position 2: "))
arr.pop(1)
arr.insert(1,new_location2)

new_location5 = str(input("Enter a new destination for position 5: "))
arr.pop(4)
arr.insert(4,new_location5)

count = 0
print('''
Updated Travel Itinerary:''')
for s in arr:
    count += 1
    print(f"{count}. {s}")