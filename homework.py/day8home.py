
class Employee:
    def __init__(self, name, role):
        self.name = name
        self.role = role

    def display(self):
        print(f"Name: {self.name}")
        print(f"Role: {self.role}")
        print("-" * 30)



class Trainer(Employee):
    def __init__(self, name, role, specialization):
        super().__init__(name, role)
        self.specialization = specialization

    def display(self):
        print(f"Name: {self.name}")
        print(f"Role: {self.role}")
        print(f"Specialization: {self.specialization}")
        print("-" * 30)



class YogaInstructor(Employee):
    def __init__(self, name, role, yoga_style):
        super().__init__(name, role)
        self.yoga_style = yoga_style

    def display(self):
        print(f"Name: {self.name}")
        print(f"Role: {self.role}")
        print(f"Yoga Style: {self.yoga_style}")
        print("-" * 30)



class MultiTrainer(Trainer, YogaInstructor):
    def __init__(self, name, role, specialization, yoga_style):
        Trainer.__init__(self, name, role, specialization)
        self.yoga_style = yoga_style

    def display(self):
        print(f"Name: {self.name}")
        print(f"Role: {self.role}")
        print(f"Specialization: {self.specialization}")
        print(f"Yoga Style: {self.yoga_style}")
        print("-" * 30)



emp = Employee("Alice Johnson", "Receptionist")
trainer = Trainer("Bob Smith", "Fitness Trainer", "Weight Training")
yoga_instructor = YogaInstructor("Clara Lee", "Yoga Instructor", "Vinyasa")
multi_trainer = MultiTrainer("David Kim", "Senior Trainer", "CrossFit", "Hatha")


emp.display()
trainer.display()
yoga_instructor.display()
multi_trainer.display()
