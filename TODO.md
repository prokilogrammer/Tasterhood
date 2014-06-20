The following are remaining work items in the order of priority
[ ] Create a simple UI with signup form and connect with backend
[ ] Figure out a method to run www outside of Django. Or something cleaner than hosting them on django static dir
[ ] Enable authentication and authorization flow with Django + TastyPie

Caveats:
1. Tastypie exposes model internals directly through its APIs. This causes tight 
   coupling with API clients and might create problems in future when changing the model. 
