from abc import ABC, abstractmethod
from datetime import datetime

class User(ABC):
    def _init_(self, name, join_year):
        self.name = name
        self.join_year = join_year

    def years_on_platform(self):
        current_year = 2025
        return current_year - self.join_year

    @abstractmethod
    def show_role(self):
        pass

    def display_info(self):
        print(f"{self.name} is a {self.show_role()} and has been on the platform for {self.years_on_platform()} years.")

class Customer(User):
    def show_role(self):
        return "Customer"

class Vendor(User):
    def show_role(self):
        return "Vendor"

c1 = Customer("Aisha", 2020)
v1 = Vendor("Rahul", 2018)

c1.display_info()
v1.display_info()