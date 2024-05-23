welcome = " Welcome to "
restaurant = " Anees Teevino's Online Restaurant "
print("\t", welcome.center(50, '*'))
print("\t", restaurant.center(50, '*'))

print("\nPlease login or register if it's your first visit.")
print("\t 1. Login")
print("\t 2. Register\n")
userinput = int(input("Select by number: "))

oldcustomers_name = {"Anees", "Kamran", "Zain"}
oldcustomers_pass = {"Anees": 123, "Kamran": 345, "Zain": 678}

if userinput == 1:
    login = " Login here !!! "
    print("\t", login.center(50, '*'), "\t \n")
    username = input("\t\tEnter username: ")
    password = int(input("\t\tEnter password: "))
    
    if username in oldcustomers_name:
        if oldcustomers_pass.get(username) == password:
            print("Login successful!")
            print("\t 1. View menu")
            oldcustomer = int(input("Select: "))
            
            if oldcustomer == 1:
                print("\t Here's our menu, sir!!! \n\t")
                menu = " Menu "
                print(menu.center(50, '*'))
                print('''\t\t\t***Appetizers***
                             1. Pakoras
                             2. Samosas
                             3. Aloo Tikki 

                        ***Soups & Salads***
                             4. Daal Soup
                             5. Kachumber Salad
                             6. Yakhni Pulao

                             ***Entrees***
                             7. Chicken Biryani
                             8. Nihari
                             9. Karahi Gosht

                        ***From the Grill***
                            10. Seekh Kebabs
                            11. Chapli Kebabs
                            12. Tandoori Chicken

                             ***Sides***
                            13. Naan
                            14. Raita
                            15. Saag

                            ***Desserts***
                            16. Gulab Jamun
                            17. Kheer
                            18. Jalebi

                           ***Beverages***
                            19. Lassi
                            20. Chai
                            21. Rooh Afza
                      \t 
                      ''')
                order = int(input("What would you like to order, sir? Enter the number: "))
                if 1 <= order <= 21:
                    print("Order confirmed! Thank you, sir.")
                else:
                    print("Invalid selection. Please try again.")
        else:
            print("Login unsuccessful! Incorrect password.")
    else:
        print("Login unsuccessful! Username not found.")
        print("click back to register !!")
else:
    print("Registration is currently unavailable. Please try again later.")
