class Student:
    def __init__(self):
        self.name = "Marian"
        self.height = 164
        self.live = 12
        self.money = 1
        self.healthy = 5
        self.happy = 25
    def GrowUp(self):
        self.height = self.height + 10
        self.live = self.live + 1
    def GrowDown(self):
        self.height = self.height - 1
    def GrowUpWithSm(self, santimeters):
        self.height = self.height + santimeters
        self.live = self.live + 1
    def BuyChvachka(self):
        self.money = self.money - 1
    def MakeGame(self):
        self.money = self.money + 10000
    def BuyChvachka1(self):
        self.money = self.money - 10000
        self.happy = self.happy - 7
        self.healthy = self.healthy - 2
        self.height = self.height + 1
    def ModifiedGame(self):
        self.money = self.money + 10000
    def GoToLikar(self):
        self.healthy = self.healthy + 1
        self.height = self.height + 2
    def BirthDay(self):
        self.money = self.money - 1100
        self.happy = self.happy + 10
        self.live = self.live + 1
        self.healthy = self.healthy + 0.5
        self.height = self.height + 3
    def DogBirthday(self):
        self.money = self.money - 1010
        self.happy = self.happy + 10
        
first_student = Student()
print (first_student.name)
print (first_student.height)
print (first_student.live)
print (first_student.money)
print (first_student.healthy)
first_student.GrowUp()
print (first_student.name)
print (first_student.height)
print (first_student.live)
print (first_student.money)
first_student.GrowDown()
print (first_student.name)
print (first_student.height)
print (first_student.live)
print (first_student.money)
sm = int(input("ведіть кількість сантиметрів"))
first_student.GrowUpWithSm(sm)
print (first_student.name)
print (first_student.height)
print (first_student.live)
print (first_student.money)
first_student.BuyChvachka()
print (first_student.name)
print (first_student.height)
print (first_student.live)
print (first_student.money)
first_student.MakeGame()
print (first_student.name)
print (first_student.height)
print (first_student.live)
print (first_student.money)
first_student.BuyChvachka1()
print (first_student.name)
print (first_student.height)
print (first_student.live)
print (first_student.money)
first_student.ModifiedGame()
print (first_student.name)
print (first_student.height)
print (first_student.live)
print (first_student.money)
first_student.GoToLikar()
print (first_student.name)
print (first_student.height)
print (first_student.live)
print (first_student.money)
print (first_student.healthy)
first_student.BirthDay()
print (first_student.name)
print (first_student.height)
print (first_student.live)
print (first_student.money)
print (first_student.healthy)
print ("Marian`s Dog:")
class Dog:
    def __init__(self):
        self.name = "Vedmedyk"
        self.height = 35
        self.live = 1
        self.healthy = 4
        self.happy = 20
    def PlayWithMarian(self):
        self.happy = self.happy + 40
    def Eat(self):
        self.happy = self.happy + 10
        self.healthy = self.healthy + 1
        self.height = self.height + 1
    def sleep(self):
        self.healthy = self.healthy + 1
        self.height = self.height + 1
        self.happy = self.happy + 10
    def birthday(self):
        self.live = self.live + 1
        self.height = self.height + 2
        self.happy = self.happy + 30
        
first_dog = Dog()
print (first_dog.name)
print (first_dog.height)
print (first_dog.live)
print (first_dog.healthy)
print (first_dog.happy)
first_dog.PlayWithMarian()
print (first_dog.name)
print (first_dog.height)
print (first_dog.live)
print (first_dog.healthy)
print (first_dog.happy)
first_dog.Eat()
print (first_dog.name)
print (first_dog.height)
print (first_dog.live)
print (first_dog.healthy)
print (first_dog.happy)
first_dog.sleep()
print (first_dog.name)
print (first_dog.height)
print (first_dog.live)
print (first_dog.healthy)
print (first_dog.happy)
first_dog.birthday()
print (first_dog.name)
print (first_dog.height)
print (first_dog.live)
print (first_dog.healthy)
print (first_dog.happy)
first_student.DogBirthday()
print (first_student.name)
print (first_student.height)
print (first_student.live)
print (first_student.money)
print (first_student.healthy)



