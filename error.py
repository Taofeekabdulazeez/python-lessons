while True:
    try:
        age = int(input("What is your age? "))
        if age < 18:
            raise Exception("You are not allowed to enter this site.")
        print(f"Your age is {age}.")
        break
    except Exception as e:
        print(e)
    except:
        print("Invalid input. please enter a number.")
 