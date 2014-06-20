from django.contrib.auth.models import User
from tastypie.resources import ModelResource
from tastypie import fields
from tastypie.authorization import Authorization

from main.models import Login, UserProfile, Contact

# Wrapper to make models sent by Tastypie to be compatible with Backbone.js
# REF: http://paltman.com/2012/04/30/integration-backbonejs-tastypie/
class BackboneCompatibleResource(ModelResource):
  class Meta:
    always_return_data = True

class ContactResource(BackboneCompatibleResource):
  class Meta:
    queryset = Contact.objects.all()
    resource_name = 'contact'

class UserProfileResource(BackboneCompatibleResource):
  contact = fields.ForeignKey(ContactResource, 'contact', full=True)

  class Meta:
    queryset = UserProfile.objects.all()
    resource_name = 'user_profile'


class UserResource(BackboneCompatibleResource):
  class Meta:
    queryset = User.objects.all()
    resource_name = 'user'
    fields = ['username']
    allowed_methods = ['get']

class LoginResource(BackboneCompatibleResource):
  user = fields.ForeignKey(UserResource, 'user', full=True)
  user_profile = fields.ForeignKey(UserProfileResource, 'user_profile', full=True)

  class Meta:
    queryset = Login.objects.all()
    resource_name = 'login'
