from django.shortcuts import render, render_to_response
from django.http import HttpResponse
from django.template import RequestContext

from main.models import Users

def index(request):
  # Get the context of the request. Context contains info such as client machine
  # details, for example.
  context = RequestContext(request)

  # Query list of registered users from the database and pass it to the view
  users_list = Users.objects.order_by('first_name')

  # Create a dictionary to pass to the template
  context_dict = {'users' : users_list}

  # Render the view and return the response
  return render_to_response('main/index.html', context_dict, context)
