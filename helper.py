from faker import Faker

faker = Faker()

def generate_registration_data():
    username = faker.user_name()
    email = f"{username}@ya.ru"
    password = faker.password(length=8, special_chars=True, digits=True, upper_case=True, lower_case=True)
    return email, password
