class Course:
    def __init__(self, course) -> None:
        print("Constructure was called")
        self.course = course # probabily list
        self.search_lecture(self.course)
        

    def search_lecture(self, lecture):
        """Return a list of lecture from the course"""
        print("Method search_lecture was called")
        # open bd and find lecture
        # if not there, offer the option to create them

    def add_lecture(self, lecture):
        """Add a lecture to the course"""
        # send to bd.py create file bd.json


        print("Method add_lecture was called")
        # open bd and add lecture