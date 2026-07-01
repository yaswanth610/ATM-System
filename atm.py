password = 1006
security_pin = 3307
balance = 10000

enter_pin = int(input("Enter the ATM PIN: "))

if enter_pin == password:
    print("** Login Success **")

    while True:
        print("\n------ ATM ------")
        print("1. DEPOSIT")
        print("2. WITHDRAW")
        print("3. BALANCE")
        print("4.CHANGE PIN")
        print("5. EXIT")

        choice = input("Enter your choice: ")

        if choice == "1":
            deposited_amount = float(input("Enter the deposit amount: "))

            if deposited_amount > 0:
                balance += deposited_amount
                print("Amount deposited successfully.")
                print("Current Balance =", balance)
            else:
                print("Invalid amount!")

        elif choice == "2":
            withdrawal_amount = float(input("Enter the withdrawal amount: "))

            if withdrawal_amount <= 0:
                print("Invalid amount!")

            elif withdrawal_amount <= balance:
                balance -= withdrawal_amount
                print("Amount withdrawn successfully.")
                print("Current Balance =", balance)

            else:
                print("Insufficient Balance!")

        elif choice == "3":
            attempts = 3

            while attempts > 0:
                pin = int(input("Enter Security PIN: "))

                if pin == security_pin:
                    print("Current Balance =", balance)
                    break

                else:
                    attempts -= 1

                    if attempts > 0:
                        print("Incorrect PIN")
                        print(attempts, "attempt(s) remaining.")
                    else:
                        print("Come again after 15 minutes.")
        elif choice == "4":
            old_pin = int(input("Enter current pin:"))
            if old_pin == security_pin:
                new_pin =int(input("Enter new pin:"))
                security_pin=new_pin
                print("Pin changed successfully")
            else:
                print("invaild pin")
        

        elif choice == "5":
            print("***** THANKS FOR VISITING *****")
            break

        else:
            print("Invalid Choice!")

else:
    print("Incorrect ATM PIN!")
