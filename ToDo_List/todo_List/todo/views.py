from rest_framework import viewsets, filters
from .models import Todo  
from .serializers import TodoSerializer

class TodoViewSet(viewsets.ModelViewSet):                             #Using ViewSet instead of function-based views for efficient CRUD operations and automatic URL routing   
    queryset = Todo.objects.all()                                     #Querying all Todo objects from the database
    serializer_class = TodoSerializer                                 #Specifying the serializer class to be used for converting model instances to JSON and vice versa     
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]  #Adding search and ordering functionality to the viewset
    search_fields = ['title', 'description']                          #Defining the fields that can be searched in the Todo model
    ordering_fields = ['created_at', 'completed']                     #Defining the fields that can be used for ordering the results

    def get_queryset(self):                                           #Overriding the get_queryset method to filter the Todo objects based on the 'completed' query parameter
        queryset = super().get_queryset()                             #Getting the base queryset from the parent class
        completed = self.request.query_params.get('completed')        #Retrieving the 'completed' query parameter from the request URL
        
        if completed is not None:                                     #To convert the string 'true' or 'false' to a boolean value            
            if completed.lower() not in ['true', 'false']:            #Checking if the value is either 'true' or 'false'
                raise ValueError("Invalid value for 'completed' parameter. Use 'true' or 'false'.")
            completed = completed.lower() == 'true'                   #Converting the string to a boolean value
            queryset = queryset.filter(completed=completed)           #Filtering the queryset based on the 'completed' status
        
        return queryset                                               #Returning the filtered queryset    