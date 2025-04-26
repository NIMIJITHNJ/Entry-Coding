from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Expense
from .forms import ExpenseForm
from django.core.paginator import Paginator
from django.db.models import Q
from django.contrib.auth.forms import UserCreationForm

def register(request):                                                  #To register new user
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'expenses/register.html', {'form': form})

@login_required                                                         #To display list of expenses with search, sort, and pagination
def expenseList(request):
    expenses = Expense.objects.filter(user=request.user)

    query = request.GET.get('q')                                        #Search
    if query:
        expenses = expenses.filter(
            Q(name__icontains=query) |
            Q(category__icontains=query) |
            Q(date__icontains=query)
        )

    sort_by = request.GET.get('sort', '')                               #Sort
    if sort_by:
        expenses = expenses.order_by(sort_by)

    paginator = Paginator(expenses, 10)                                 #Pagination - 10 expenses per page
    page = request.GET.get('page')
    expenses = paginator.get_page(page)

    return render(request, 'expenses/expenseList.html', {'expenses': expenses})

@login_required
def expenseCreate(request):                                            #To create a new expense
    expense = None 
    if request.method == 'POST':        
        form = ExpenseForm(request.POST)
        if form.is_valid():
            expense = form.save(commit=False)
            expense.user = request.user
            expense.save()
            return redirect('expenseList')
    else:
        form = ExpenseForm()
    return render(request, 'expenses/expenseForm.html', {'form': form})

@login_required
def expenseUpdate(request, pk):                                        #To update an existing expense
    expense = get_object_or_404(Expense, pk=pk, user=request.user)
    if request.method == 'POST':
        form = ExpenseForm(request.POST, instance=expense)
        if form.is_valid():
            form.save()
            return redirect('expenseList')
    else:
        form = ExpenseForm(instance=expense)
    return render(request, 'expenses/expenseForm.html', {'form': form, 'expense': expense})

@login_required
def expenseDelete(request, pk):                                        #To delete an expense
    expense = get_object_or_404(Expense, pk=pk, user=request.user)
    if request.method == 'POST':
        expense.delete()
        return redirect('expenseList')
    return render(request, 'expenses/expenseConfirm.html', {'expense': expense})