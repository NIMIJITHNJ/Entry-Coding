from django.db import models

class Todo(models.Model):                                   #Defining a Todo model with fields for title, description, completed status, and timestamps    title = models.CharField(max_length=200)
    description = models.TextField()                        #A text field for a detailed description of the task
    title = models.CharField(max_length=200)                #A character field for the title of the task
    completed = models.BooleanField(default=False)          #A boolean field to indicate if the task is completed
    created_at = models.DateTimeField(auto_now_add=True)    #A timestamp field for when the task was created
    updated_at = models.DateTimeField(auto_now=True)        #A timestamp field for when the task was last updated

    def __str__(self):                                      #A string representation of the model, returning the title of the task
        return self.title                       