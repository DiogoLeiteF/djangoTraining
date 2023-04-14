import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'testProj.settings')

import django

django.setup()

## FAKE POP SCRIPT
import random
from appTest.models import Topic, Webpage, AccessRecord
from faker import Faker

fakegen = Faker()


## for Topic use a selections of topics

topics = ['Search', 'Social', 'Marketplace', 'News', 'Games']
def add_topic():
    t = Topic.objects.get_or_create(top_name = random.choice(topics))[0]
    t.save()
    return t


## for Webpage and AccessRecord use faker
def populate(N=5):
    for entry in range(N):

        # get the topic for the entry
        top = add_topic()

        # create the fake data for that entry
        fake_url = fakegen.url()
        fake_date = fakegen.date()
        fake_name = fakegen.company()

        # Create the new webpage entry
        webpg = Webpage.objects.get_or_create(topic = top, url = fake_url, name = fake_name)[0]

        # create fake accessrecord entry
        acc_rec = AccessRecord.objects.get_or_create(name = webpg, date = fake_date)[0]

if __name__ == "__main__":
    print("populating script!")
    populate(20)
    print("populating complete!")