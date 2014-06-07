from django.db import models

# Tasterhood's main models

class Contacts(models.Model):
  addr_line1 = models.CharField(max_length=512)
  addr_line2 = models.CharField(max_length=255, null=True)
  city = models.CharField(max_length=255)
  state = models.CharField(max_length=255)
  country = models.CharField(max_length=255)
  zipcode = models.IntegerField()
  email = models.EmailField(max_length=255)
  phone1 = models.CharField(max_length=32, null=True)
  phone2 = models.CharField(max_length=32, null=True)
  website = models.URLField(max_length=512, null=True)

  def __unicode__(self):
    return self.addr_line1 + ", " + self.city + ", " + self.state + " - " + `self.zipcode`


class Users(models.Model):

  # Types of users
  TASTER = "taster"
  RESTAURANT_OWNER = "owner"
  USER_TYPES = (
      (TASTER, "Taster"),
      (RESTAURANT_OWNER, "Restaurant owner")
      )

  first_name = models.CharField(max_length=255)
  last_name = models.CharField(max_length=255, null=True)
  contact = models.ForeignKey(Contacts)
  created_at = models.DateField(auto_now_add=True)
  user_type = models.CharField(max_length=16, choices=USER_TYPES, default=TASTER)
  cuisine_pref = models.TextField(null=True)  # Future(sanath): This should be a JSON field
  location_pref = models.TextField(null=True)  # Future(sanath): This should be a JSON field

  def __unicode__(self):
    return self.first_name + " (" + self.user_type + ")"


class Login(models.Model):
  username = models.CharField(max_length=255, unique=True)
  password = models.CharField(max_length=255)
  user = models.ForeignKey(Users)
  last_login = models.DateField(null=True)

  def __unicode__(self):
    return self.username


class Restaurants(models.Model):
  name = models.CharField(max_length=255)
  owner = models.ForeignKey(Users)
  contact = models.ForeignKey(Contacts)
  created_at = models.DateField(auto_now_add=True)
  cuisines = models.TextField(null=True)
  specialities = models.TextField(null=True)

  def __unicode__(self):
    return self.name


class Offers(models.Model):

  # Offer categories
  DISCOUNT = "discount"
  FREEBIE = "freebie"
  OFFERS_CATEGORIES = (
      (DISCOUNT, "Discount"),
      (FREEBIE, "Get a freebie")
      )

  restaurant = models.ForeignKey(Restaurants)
  description = models.TextField()
  created_at = models.DateField(auto_now_add=True)
  category = models.CharField(max_length=128, choices=OFFERS_CATEGORIES, default=DISCOUNT)
  cupon_link = models.URLField(max_length=512, null=True)

  def __unicode__(self):
    return self.category + " at " + self.restaurant.name

