from django.shortcuts import render
from django.urls import reverse
from Website.models import AccessRecord, Topic, Webpage, UserProfileInfo
from Website.forms import UserForm, UserProfileInfoForm
# from Website.forms import NewUser
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth import authenticate, login, logout

# Create your views here.
def index(request):
    webpage_list = AccessRecord.objects.order_by('date')
    date_dict = {'access_records': webpage_list}
    
    return render(
        request,
        'Website/index.html',
        context=date_dict
    )


# def user(request):
#     user_list = User.objects.order_by('first_name')
#     user_dict = {'user_lists': user_list}
#     return render(
#         request,
#         'Website/view_user.html',
#         context=user_dict
#     )

def register(request):
    registered = False

    if request.method == 'POST':
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileInfoForm(data=request.POST)
        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            user.set_password(user.password) # Hashing the password 
            user.save()

            profile = profile_form.save(commit=False) # Not save to database at first
            profile.user = user # map the profile to user 
            if 'profile_pic' in request.FILES: # Check if have a profile picture 
                profile.profile_pic = request.FILES['profile_pic']
            
            profile.save()
            registered = True

        else:
            print(user_form.errors, profile_form.errors)
    else:
        user_form = UserForm()
        profile_form = UserProfileInfoForm()
    return render(
        request,
        'Website/register.html',
        {'user_form': user_form, 'profile_form': profile_form, 'registered': registered}
    )


def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username') # Retrieve username from a form 
        password = request.POST.get('password') # Retrieve password from a form
        user = authenticate(username=username, password=password) # authen user 

        if user:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect(reverse('index'))
            else:
                return HttpResponse('Account not active')
            
        else:
            print("Someone tried to login and failed!")
            return HttpResponse("invalid login details supplied!")
    else:
        return render(
            request,
            'Website/login.html',
            {}
        )
    

@login_required # to access this need to login first 
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))
# def signup(request):
#     form = NewUser()

#     if request.method == 'POST':
#         form = NewUser(request.POST)
#         if form.is_valid():
#             form.save(commit=True) # This step is save data into the database
#             return user(request) # After that go to the next page, in this case is user page 

#     return render(
#         request,
#         'Website/signup.html',
#         {'form': form}
#     )

def help(request):
    my_dict = {'name': "Hung OK"}
    return render(request, 'Website/help.html', context=my_dict)