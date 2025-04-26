from django import forms
from .models import Expense

class ExpenseForm(forms.ModelForm):                                     #Form to create and update Expenses
    class Meta:
        model = Expense
        fields = ['name', 'amount', 'category', 'date', 'description']
        
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'}),
        }