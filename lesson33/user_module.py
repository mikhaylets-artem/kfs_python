class User:
    def __init__(self, first_name, last_name, age, phone, work, login_attempts):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.phone = phone
        self.work = work
        self.login_attempts = login_attempts

    def describe_user(self):
        print(f"Ваc зовут :{self.first_name} {self.last_name}")

    def greeting_user(self):
        print(f"Hello,{self.first_name} {self.last_name}")

    def increment_login_attempts(self):
        self.login_attempts += 1
        print(self.login_attempts)

    def reset_login_attempts(self):
        self.login_attempts = 0
        print(self.login_attempts)


x = User("Artem", "Mikhaylets", 16, "+380958838458", "KPL", 0)
# x.describe_user()
# x.greeting_user()
# x.increment_login_attempts()
# x.increment_login_attempts()
# x.increment_login_attempts()
# x.reset_login_attempts()
# x.increment_login_attempts()
