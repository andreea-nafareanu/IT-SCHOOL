from faker import Faker
fake = Faker("ro_RO")

for i in range(100):
    print (fake.name())