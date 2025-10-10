#CS2Q2 - Programming Task 2: Delivery Fee Calculator

'''
Goal
• Your task is to compute a delivery fee based on distance and a fixed rate per kilometer.

Role
• You are a programmer for a food delivery app.

Audience
• The target audience is delivery customers who want to know their delivery charges before placing an order.

Situation
• The context you find yourself in is a local delivery service setting pricing for various distances.

Product, Performance, and Purpose
• You will create a function in order to calculate and return the total delivery fee.

Standards and Criteria for Success
• Your function must return the correct fee and work with any distance or rate input.
'''

def delivery_fee(km,rate):
    fee = km*rate
    if fee < 0:
        print("Error!")
        return
    else:
        return fee

# --- Main Program ---

km_input = float(input("Enter distance in kilometers:"))
rate_input = float(input("Enter rate per kilometer (₱):"))

delivery_fee(km_input,rate_input)
print(f"Total Delivery Fee: ₱{delivery_fee(km_input,rate_input):.2f}")
