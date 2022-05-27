# Light the LED
def light_led(number):
    layer = 1
    
    while layer <= 5:
        leds_layer = get_leds_in_layer(layer)
        light = ""
        
        for n in number:
            str_num = check_number(n)
            
            for i in leds_layer:
                if i in str_num:
                    light += "#"
                else:
                    light += " "
                
            light += " "
                    
        print(light)
        layer += 1

# Check input number
def check_number(num):
    str_num = None
    
    if int(num) == 1:
        str_num = [3, 6, 9, 12, 15]
    elif int(num) == 2:
        str_num = [1, 2, 3, 6, 7, 8, 9, 10, 13, 14, 15]
    elif int(num) == 3:
        str_num = [1, 2, 3, 6, 7, 8, 9, 12, 13, 14, 15]
    elif int(num) == 4:
        str_num = [1, 3, 4, 6, 7, 8, 9, 12, 15]
    elif int(num) == 5:
        str_num = [1, 2, 3, 4, 7, 8, 9, 12, 13, 14, 15]
    elif int(num) == 6:
        str_num = [1, 2, 3, 4, 7, 8, 9, 10, 12, 13, 14, 15]
    elif int(num) == 7:
        str_num = [1, 2, 3, 6, 9, 12, 15]
    elif int(num) == 8:
        str_num = [1, 2, 3, 4, 6, 7, 8, 9, 10, 12, 13, 14, 15]
    elif int(num) == 9:
        str_num = [1, 2, 3, 4, 6, 7, 8, 9, 12, 13, 14, 15]
    elif int(num) == 0:
        str_num = [1, 2, 3, 4, 6, 7, 9, 10, 12, 13, 14, 15]
    
    return str_num

# Get the LED per layer
def get_leds_in_layer(layer):
    leds_layer = None
    
    if layer == 1:
        leds_layer = [1, 2, 3]
    elif layer == 2:
        leds_layer = [4, 5, 6]
    elif layer == 3:
        leds_layer = [7, 8, 9]
    elif layer == 4:
        leds_layer = [10, 11, 12]
    elif layer == 5:
        leds_layer = [13, 14, 15]
    
    return leds_layer

number = ""

while True:
    number = input("Enter number: ")
    
    try:
        int(number)
        break
    except ValueError:
        continue

light_led(number)