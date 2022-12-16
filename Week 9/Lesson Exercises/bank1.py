balance = 0

def main():
    print("Balance: ", balance)
    deposit(100)
    withdraw(25)
    print("Balance: ", balance)

def deposit(amount):
    global balance
    balance += amount

def withdraw(amount):
    global balance
    balance -= amount


if __name__ == "__main__":
    main()