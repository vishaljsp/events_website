import os
# from app1.models import m1
from faker import Faker
import django

# os.environ.setdefault('DJANGO_SETTINGS_MODULE','p1.settings')

# django.setup()

fake = Faker()
def pop(n=10):

    for i in range(n):
        fake_name1 = fake.name()

        fake_name2 = fake.name()

        fake_email = fake.email()
        
        print(fake_name1)

        # nm1.objects.get_or_create(first_name=fake_name1,last_name=fake_name2,email=fake_email)



if __name__ == '__main__':
    print("Populating")
    pop(50)
    print("complete")