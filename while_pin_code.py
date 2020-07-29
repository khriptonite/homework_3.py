####DATA LAYER
CLIENT_SECRET_PIN = 1234
CLIENT_FULL_NAME  = "John Doe"
CLIENT_BANK_ID    = "123abc567xyz"


####LOCIC & USER INTERFACE
user_pin = 0
stop_pin = 0

while user_pin != CLIENT_SECRET_PIN:
    
    user_pin = int(input("PIN: "))
    stop_pin += 1
    if user_pin == CLIENT_SECRET_PIN:
        break
    elif stop_pin == 3:
        break
    
