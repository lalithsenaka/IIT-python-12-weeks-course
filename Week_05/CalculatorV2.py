while True:

    print("*** Calculator ***")
    print("1.Addition")
    print("2.Subtraction")
    print("3.Multiplication")
    print("4.Division")
    print("5.Exit")

    # read menu choice
    try:
        choice=int(input("Enter the choice ?").strip())
    except ValueError:
        print("Please insert correct number for choice ?")
        continue


    if choice==1:
        num1=float(input("Enter the first number ?"))
        num2=float(input("Enter the second number ?"))
        answer=num1+num2
        print(f"Answer is: {answer}")

    elif choice==2:
        num1=float(input("Enter the first number ?"))
        num2=float(input("Enter the second number ?"))
        answer=num1-num2
        print(f"Answer is: {answer}")

    elif choice==3:
        num1=float(input("Enter the first number ?"))
        num2=float(input("Enter the second number ?"))
        answer=num1*num2
        print(f"Answer is: {answer}")

    elif choice==4:
        num1=float(input("Enter the first number ?"))
        num2=float(input("Enter the second number ?"))
        if num2!=0:
            answer=num1/num2
        else:
            print("Invalid value, please enter non zero number ?")
        print(f"Answer is: {answer}")

    elif choice==5:
        print("Good bye,Thank you")
        break

    else:
        print("Invalid number, please selct correct number for choice")

                    
