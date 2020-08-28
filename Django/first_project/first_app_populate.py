import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'first_project.settings')

import django
django.setup()

import random
from first_app.models import Topic, Webpage, AccessRecord
from faker import Faker

f = Faker()
topics = ['Search Engine', 'Social Network', 'News', 'Games', 'ECommerce']

def add_topic():
    t = Topic.objects.get_or_create(top_name = random.choice(topics))[0]
    t.save()
    return t

def populate(n = 5):
    for i in range(n):
        #Topic generated
        t = add_topic()

        #Fake data
        name = f.company()
        url = f.url()
        date = f.date()

        #Create Models
        w = Webpage.objects.get_or_create(topic = t, name = name, url = url)[0]
        w.save()

        a = AccessRecord.objects.get_or_create(name = w, date = date)[0]
        a.save()

if __name__ == '__main__':
    populate(10)
