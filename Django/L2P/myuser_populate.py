import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'L2P.settings')

import django
django.setup()

from myuser.models import User_details
from faker import Faker

f = Faker()

def populate(n = 5):
    for i in range(n):
        name = f.name().split(' ')
        fname = name[0]
        lname = name[1]
        em = f.email()

        u = User_details.objects.get_or_create(first_name = fname, last_name = lname, email = em)[0]
        u.save()


if __name__ == '__main__':
    populate(5)
