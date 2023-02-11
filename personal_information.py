from course import Course


class Person:
    def __init__(self, name, course) -> None:
        self.name = name
        self.course = Course(course)