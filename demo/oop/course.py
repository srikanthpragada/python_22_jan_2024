class Course:
    # static attribute or class attribute
    hourlyPrice = 500

    @staticmethod
    def setHourlyPrice(newPrice):
        Course.hourlyPrice = newPrice

    def __init__(self, title, duration):
        # object attributes
        self.title = title
        self.duration = duration

    def show(self):
        print(f"Title   : {self.title}")
        print(f"Duration: {self.duration}")

    def getfee(self):
        return self.duration * Course.hourlyPrice


c1 = Course("Python", 20)
c2 = Course("AWS", 15)
Course.setHourlyPrice(600)
c1.show()
print(c1.getfee())



