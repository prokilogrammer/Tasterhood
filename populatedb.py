import os

def populate():
  print "Creating Ramya"
  contact1 = Contacts(addr_line1 = "18570 NE 58th Ct, #K3084", city = "Redmond", state = "WA", country="USA", zipcode = 98052, email = "ramyaramaswamy89@gmail.com")
  contact1.save()
  user1 = UserProfile(first_name = "Ramya", contact=contact1)
  user1.save()

  print "Creating Sanath"
  contact2 = Contacts(addr_line1 = "2 Arundel Road, #2", city = "Burlingame", state = "CA", country="USA", zipcode = 94010, email = "dayanandasaraswati@gmail.com")
  contact2.save()
  user2 = UserProfile(first_name = "Sanath", contact=contact2)
  user2.save()

if __name__ == '__main__':
  os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'tasterhood.settings')
  from main.models  import Contacts, UserProfile
  populate()
