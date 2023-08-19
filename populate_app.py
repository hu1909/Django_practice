import os 
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'web_project.settings')
django.setup()


## fake pop script 
import random
from Website.models import AccessRecord, Topic, Webpage, User
from faker import Faker

fakegen = Faker()
topics = ['Search', 'Social', 'Marketpace', 'News', 'Games']

def add_topic():
    t = Topic.objects.get_or_create(top_name=random.choice(topics))[0] 
    t.save()
    return t 

def populate(N=5):
    for entry in range(N):
        top = add_topic()

        # Create a fake data for the entry 
        fake_url = fakegen.url()
        fake_date = fakegen.date()
        fake_name = fakegen.company()
        fake_firstname = fakegen.first_name()
        fake_lastname = fakegen.last_name()
        fake_mail = fakegen.email()

        user_acc = User.objects.get_or_create(first_name=fake_firstname, last_name= fake_lastname, email=fake_mail)[0]

        # Create the new webpage entry 
        webpg = Webpage.objects.get_or_create(topic= top, url=fake_url, name=fake_name)[0]

        # Create a fake access record for that webpage 
        acc_rec = AccessRecord.objects.get_or_create(name=webpg, date=fake_date)[0]
        






if __name__ == '__main__':
    print("Populating script!")
    populate(20)
    # add_User(20)
    print("populated script")