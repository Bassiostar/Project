class student:
    grade = 10
    name = "Steve"
    def intro(self):
        print("Hello, I'm a student")

    def details(self):
        print("My name is ",self.name)
        print("I study in grade ", self.grade)

ob=student()
ob.intro()
ob.details()