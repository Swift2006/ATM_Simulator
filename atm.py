class Atm:
# Data required:-
# Balance (-)
# ATM Pin (-)
# Counter Serial Number (-)

# Functions required:-
# Create Pin (+) (->getter (+) & ->setter (+))
# Withdraw (+)
# Deposit (+)
# Check balance (+)
# Serial Number (+) (-> getter(+) & setter(+))

    __counter = 1    #   (initial Serial Number) Static/Class Variable

    # Constructor
    def __init__(self):            # a constructor code executes primarily and sequestially 
        self.__pin = None          # WE ARE USING SELF.PIN AND SELF.BALANCE BECAUSE EVERY DIFFERRENT OBJECT WILL HAVE ITS UNIQUE PIN AND UNIQUE BALANCE
        self.__balance = 0         # Initializing the balance
        self.__create_pin()         # to create a pin before taking any further actions 
        self.sno = Atm.__counter   # Instance Variable
        Atm.__counter += 1         # Updating Serial Number 

    @staticmethod
    def get_counter():              # To get the current seriel Number 
        return Atm.__counter
    @staticmethod
    def set_counter(new):           # To set/update the current Serial Number 
        if type(new) == int:
            Atm.__counter = new
        else:
            print("Not Allowed!😒")

# Asking user to create a pin
    def __create_pin(self):
        self.__pin = int(input("Create an ATM Pin before proceeding further: "))
        print("Pin Created sucessfully!")
        print()


# To Change the current pin & It will take 1(new_pin) arguement (technicaly 2 -> self and new_pin)
    def set_pin(self):        # --> setter
        new_pin = int(input("Create a new Pin: "))
        if type(new_pin) == int:
            self.__pin = new_pin
            print("Pin Changed!🤫")
        else:
            print("Not Allowed!😒")
# To Know the Changed Pin
    def get_pin(self):      #  --> getter
        print("Your current Pin is: {}".format(self.__pin))
    

# Asking user to enter the previously created pin and then checking if it is correct or not. if yes, then adding the deposit amount to balance!
    def deposit(self):
        temp = int(input("Enter Your recently created pin: "))
        if temp == self.__pin:
            amount = int(input("Enter the Amount you want to Deposit: "))
            self.__balance += amount
            print("Deposit sucessful!💸")
        else:
            print("Invalid Pin!😟")


# Withrawal according to the balnce available in the account 
    def withdrawal(self):
        temp = int(input("Enter Your recently created pin: "))
        if temp == self.__pin:
            amount = int(input("Enter the amount you want to withdraw: "))
            if amount <= self.__balance:
                self.__balance -= amount
            else:
                print("Insuffecient Balance!😓")
        else:
            print("Invalid Pin!😟")
       
    
# Checking Balance 
    def check_balance(self):
        temp = int(input("Enter Your recently created pin: "))
        if temp == self.__pin:
            print(self.__balance)
        else:
            print("Invalid Pin!😟")
