from django.shortcuts import render, render_to_response
from django.http import HttpResponse
from django.template import RequestContext

def index(request):
  # Get the context of the request. Context contains info such as client machine
  # details, for example.
  context = RequestContext(request)

  # Create a dictionary to pass to the template
  context_dict = {'message' : 'Yo honey singal'}

  # Render the view and return the response
  return render_to_response('main/index.html', context_dict, context)
