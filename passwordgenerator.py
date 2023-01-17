import random
import string

def password_details():     
       
    choices = ["up", "low", "sym", "num", "space", 'exit']

    choice_meaning ={
        "up"    : "Uppercase",
        "low"   : "Lowercase",
        "sym"   : "Symbols",
        "num"   : "Numbers",
        "space" : "Space",
    }
     
    values_list = []
    for values in choice_meaning.values():
        values_list.append(values)    
    print(values_list) 
    
    chosen_list = []
    chosen_details = input("Select Your desired features from the list above[up, low, sym, num, space]: ")
    low_chosen_details = chosen_details.lower() 
    if low_chosen_details in choices :
            chosen_list.append(low_chosen_details)
    else:
            print("OOPS! It's wrong please enter correct form like example.")
    while low_chosen_details != "exit" :
            chosen_details = input("Select Your desired features from the list above[up, low, sym, num, space]: ")
            low_chosen_details = chosen_details.lower() 
            if low_chosen_details in chosen_list:
                print("OOPS! It's chosen before.")
            
            elif low_chosen_details in choices :
                    chosen_list.append(low_chosen_details)

            else:
                    print("OOPS! It's wrong please enter correct form like example.")
            
    chosen_list.pop()  
    return chosen_list

def make_password():
    pass_lenght = int(input("How many character does it have? "))
    user_choices = password_details()
    ai_choices_list = []
    
    for _ in range (1 , pass_lenght + 1): 
                        
        ai_choice = random.choice(user_choices)
        ai_choices_list.append(ai_choice)
        
    return ai_choices_list
                                                   
def generate_random_character():
    uppercase = string.ascii_uppercase
    lowercase = string.ascii_lowercase
    symbols = ["#", "@", "!", "%", "*", "_", "-", "&", "$", "?"]
    numbers = [0,1,2,3,4,5,6,7,8,9]
    
    final_pass = []
    
    for i in make_password():
        if i == 'low':
            final_pass.append(random.choice(lowercase))
        elif i == 'up':
            final_pass.append(random.choice(uppercase))            
        elif i == 'sym':
            final_pass.append(random.choice(symbols))            
        elif i == 'num':
            final_pass.append(random.choice(numbers))    
        elif i == 'space':
            final_pass.append(" ")        
            
    return final_pass  

def list_to_string():
    password_str = ''.join(map(str, generate_random_character()))
    
    return password_str

def generate_password_again():
    while True:
        gen_again = input("Do you want to try again?[ yes , no]:")
        low_gen_again = gen_again.lower()
        if low_gen_again in ["yes", "no"]:
            if low_gen_again == "yes":
                generate_random_character()
                
            if low_gen_again == "no":
                print('Thank you for choosing us.')
                break     
        else:
            print('InValid Input.(Choose from {y: yes, n: no, enter: yes}).')
            print('Try again.') 
            
                                   
print(list_to_string())  
generate_password_again()   


