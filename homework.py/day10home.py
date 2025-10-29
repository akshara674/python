from abc import ABC, abstractmethod  

class User(ABC):
    def _init_(self, name, account_year):
        self.name = name
        self.account_year = account_year

    def account_age(self):
        current_year = 2025
        return current_year - self.account_year

    @abstractmethod
    def get_role(self):
        pass

class Admin(User):
    def get_role(self):
        return "Admin"

    def _str_(self):
        return f"Admin User: {self.name}, Account created in {self.account_year}"

class Guest(User):
    def get_role(self):
        return "Guest"

    def _str_(self):
        return f"Guest User: {self.name}, Account created in {self.account_year}"


admin_user = Admin("Abhi", 2020)
guest_user = Guest("Riya", 2023)

print(f"Role: {admin_user.get_role()}, Account Age: {admin_user.account_age()} years")
print(admin_user)   

print(f"Role: {guest_user.get_role()}, Account Age: {guest_user.account_age()} years")
print(guest_user)