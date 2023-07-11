# Challenge 1: Square Numbers and Return Their Sum

class Point:
    def __init__(self,x,y,z):
        self.x = x
        self.y = y
        self.z = z

    def sum_square(self):
        return self.x**2 + self.y**2 + self.z**2
Point = Point(1, 3, 5)
print(Point.sum_square())


#Challenge 2: Implement a Calculator Class

class Calculator:
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2
    def add(self):
        return self.num1 + self.num2

    def subtract(self):
        return self.num2 - self.num1

    def multiply(self):
        return self.num1 * self.num2

    def divide(self):
        return self.num2 / self.num1

obj = Calculator(10, 94)
print(obj.add())
print(obj.subtract())
print(obj.multiply())
print(obj.divide())


# Challenge 3: Implement the Complete Student Class

class Student:
    def __init__(self):
        self.__name = ""
        self.__rollNumber = ""

    def getName(self):
        return self.__name
    
    def setName(self, name):
        self.__name = name

    def getRollNumber(self):
        return self.__rollNumber

    def setRollNumber(self, rollNumber):
        self.__rollNumber = rollNumber   

student = Student()

student.setName("John Doe")

student.setRollNumber("2021001")

print(student.getName())

print(student.getRollNumber())


# Challenge 4: Implement a Banking Account

class Account:
    def __init__(self, title, balance):
        self.title = title
        self.balance = balance

class SavingsAccount(Account):
    def __init__(self, title, balance, interestRate):
        super().__init__(title, balance)
        self.interestRate = interestRate

account = Account("Ashish", 5000)
Savings_account = SavingsAccount("ashish", 5000, 5)

print(account.title)
print(account.balance)
print(Savings_account.title)
print(Savings_account.balance)
print(Savings_account.interestRate)


# Challenge 5: Handling a Bank Account

class Account:
    def __init__(self, title=None, balance=0):
        self.title = title
        self.balance = balance
    
    def withdrawal(self, amount):
        if amount <= self.balance:
            self.balance -= amount
        else:
            print("Insufficient balance")

    def deposit(self, amount):
        self.balance += amount
    
    def getBalance(self):
        return self.balance

class SavingsAccount(Account):
    def __init__(self, title=None, balance=0, interestRate=0):
        super().__init__(title, balance)
        self.interestRate = interestRate
    
    def interestAmount(self):
        return self.balance * self.interestRate / 100


demo1 = SavingsAccount("Ashish", 2000, 5)   
demo1.deposit(500)
print(demo1.getBalance())  

demo1.withdrawal(1000)
print(demo1.getBalance()) 

interest = demo1.interestAmount()
print(interest)  

