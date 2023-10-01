def is_input_float(num):
    try:
        num1=float(num)
        return num1
    except:
        return None

def take_temperature_input(message_to_user):
    choice = False
    while not choice:
        temp=input(message_to_user)
        temp=is_input_float(temp)
        if temp !=None:
            choice=True
            return temp
        print("Please enter a valid Temperature such as 26 or 37.6! ")
