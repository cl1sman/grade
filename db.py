import json

class DataBase:
    def __init__(self) -> None:
        pass
    
    def create(self, lecture_name):
        self.lecture_name = lecture_name
        # first note, second weight
        number_of_notes = [[0, 0]] * int(input("Number of notes:> "))
        # for i in range(number_of_notes):
        # call grade to create the dict?
        lecture = {
            self.lecture_name: number_of_notes
            # key : [value1, value2, value3]
        }

        with open('db.json', "w") as file:
            file.write(json.dumps(lecture, indent=4))
    
    def check(self):
        pass

a = DataBase()
a.create("FTC")