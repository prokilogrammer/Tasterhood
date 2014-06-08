from django.contrib.auth.models import User
from tastypie.resources import ModelResource
from tastypie import fields
from tastypie.authorization import Authorization

from main.models import Login, UserProfile, Contact

class ContactResource(ModelResource):
  class Meta:
    queryset = Contact.objects.all()
    resource_name = 'contact'

class UserProfileResource(ModelResource):
  contact = fields.ForeignKey(ContactResource, 'contact', full=True)

  class Meta:
    queryset = UserProfile.objects.all()
    resource_name = 'user_profile'


class UserResource(ModelResource):
  class Meta:
    queryset = User.objects.all()
    resource_name = 'user'
    fields = ['username']
    allowed_methods = ['get']

class LoginResource(ModelResource):
  user = fields.ForeignKey(UserResource, 'user', full=True)
  user_profile = fields.ForeignKey(UserProfileResource, 'user_profile', full=True)

  class Meta:
    queryset = Login.objects.all()
    resource_name = 'login'
