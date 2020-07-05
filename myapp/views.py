from django.shortcuts import render
from django.http import HttpResponse
from myapp.forms import UserForm
# Create your views here.

def user(request):

    user_list = User.objects.order_by('first_name')
    user_dict = {'users': user_list}
    return render(request, 'user.html', context=user_dict)

def index(request):
    return render (request, 'index.html')

def home(request):
    return HttpResponse('<h1>hi hello namaste </h1>')

def userforms(request):
    form = UserForm()

    if request.method == "POST":
        form = UserForm(request.POST)

        if form.is_valid():
            print("The Form Is Valid! ")
            form.save(commit=True)
            return index(request)
        else:
            print("The Form Is Not Valid! ")
    return render(request, 'userform.html', {'form':form})
