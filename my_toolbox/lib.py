def born():
    while True:
        try:
            your_age = input("How old are you? ")
            your_age = abs(int(float(your_age)))
            break
        except:
            print("Invalid input, please provide an integer")
            
    while True:
        try:
            your_month = input("Which month were you born? ")
            if your_month.lower() in ['january', 'february', 'march', 'april', 'may', 'june', 'july', \
                'august', 'september', 'october', 'november', 'december']:
                break
            else:
                print("Please provide your month written out and not as a number.")
        except:
            print("Please provide your month written out and not as a number.")
    
    if your_month.lower() in ['january', 'february', 'march', 'april', 'may']:
        born = 2021 - int(your_age)
    else:
        born = 2020 - int(your_age)
        
    print(f'You were born {born}!')
    
if __name__ == "__main__":
    born()