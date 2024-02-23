import json
class Course:
    def __init__(self, title, fee):
        self.title = title
        self.fee = fee


c = Course("Java EE", 10000)
print(json.dumps(c.__dict__))

