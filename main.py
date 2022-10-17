User_Input =input("Do you want to print(p) or exit without printing(q) :")

while(User_Input):
    if(User_Input=="p"):
      print("Hello")
      User_Input =input("Do you want to print(p) or exit without printing(q) :")
    elif(User_Input=="q"):
        User_Input= False
    else:
        break
print("This is a valid code for testing the feature")