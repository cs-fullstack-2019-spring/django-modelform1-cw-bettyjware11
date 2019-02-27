from django.shortcuts import render
from django.http import HttpResponse
from .forms import NewUserForm

# function to test with.
def index(request):
    return HttpResponse("exerciseApp")

# function to provide a page to add users
def indexOfUsers(request):
    new_form = NewUserForm
    if request.method == "POST":
        print("Posted Data from Bloggers")
        new_form = NewUserForm(request.POST) #empty form extracts all data that was put into form
        if new_form.is_valid():
            new_form.save(commit=True) #immediately commit and save to database
            return indexOfUsers(request) #goes back home
        else:
            print('Error Not Valid')


    return render(request, 'exerciseApp/indexOfUsershtml', {'userform': new_form} )



