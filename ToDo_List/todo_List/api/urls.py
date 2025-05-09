from django.urls import path, include
from rest_framework.routers import DefaultRouter
from todo.views import TodoViewSet

router = DefaultRouter()                                    #Creating a router object to manage the URL routing for the API
router.register(r'todos', TodoViewSet, basename='todo')     #Registering the TodoViewSet with the router, associating it with the URL prefix 'todos' and giving it a basename of 'todo'
# The router will automatically generate the necessary URL patterns for the CRUD operations of the TodoViewSet
# The basename is used to create the URL names for the viewset actions (list, create, retrieve, update, destroy)
urlpatterns = [                                             #Defining the URL patterns for the API
    path('', include(router.urls)),                         #Including the router-generated URL patterns
]