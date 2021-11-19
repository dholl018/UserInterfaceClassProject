from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.shortcuts import get_object_or_404
from django.contrib.auth import authenticate
from django.http import JsonResponse

# Create your views here.
from actions.models import Action


def profile(request, username):
    user1 = get_object_or_404(User, username=username)
    action = Action.objects.filter(user=user1)
    return render(request,
                  "users/user/profile.html",
                  {"user": user1, "actions": action},
                  )


def edit_profile(request, username):
    user1 = get_object_or_404(User, username=username)
    return render(request,
                  "users/user/editprofile.html",
                  {"user": user1}
                  )


def edit_profile_subit(request, username):
    if request.method == 'POST':
        first_name = request.POST.get("firstname")
        # date = request.POST.get("updated_date")
        last_name = request.POST.get("lastname")
        password = request.POST.get("retypePassword")
        role = request.POST.get("role")
        actorUsername = request.session["username"]
        actor = User.objects.get(username=actorUsername)
        user = User.objects.get(username=username)
        previousRole = user.details.role
        user.last_name = last_name
        user.first_name = first_name
        user.set_password(password)
        user.details.role = role
        user.save()
        if previousRole != role:
            if role == 'admin':
                action = Action(
                    user=actor,
                    verb="Has upgraded a user to admin.",
                    target=user,
                )
                action.save()
            else:
                action = Action(
                    user=actor,
                    verb="Has changed a user role",
                    target=user,
                )
                action.save()
        # Redirect to detail view
        messages.add_message(request, messages.INFO, "User: %s details has been edited" % user.username)
        return render(request,
                      "users/user/profile.html",
                      {'user': user}
                      )


def signup(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        firstName = request.POST.get('fname')
        lastName = request.POST.get('lname')
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = User.objects.create_user(username, email, password)
        user.first_name = firstName
        user.last_name = lastName
        user.save()
        action = Action(
            user=user,
            verb="Has joined the site",
            target=user,
        )
        action.save()
        messages.add_message(request, messages.SUCCESS, "You have successfully registered: %s" % user.username)
        return redirect('safety:home_user_logged_in')
    else:
        return render(request,
                  "users/user/signup.html",
                  )


def signup_check(request):
    is_ajax = request.headers.get('x-requested-with') == 'XMLHttpRequest'
    if is_ajax and request.method == "POST":
        query = request.POST.get('typed_data')
        results = User.objects.filter(username__iexact=query)
        username_id = request.POST.get('username_id')
#        typed_data = request.POST.get('typed_data')
        try:
            if results:
                return JsonResponse({'error': 'username taken'}, status=200)
            else:
                return JsonResponse({'success': 'success'}, status=200)
        except User.DoesNotExist:
            return JsonResponse({'success': 'success'}, status=200)
    else:
        return JsonResponse({'error': 'invalid Ajax request'}, status=400)


def login_user(request):
    username = request.POST.get("username")
    pw = request.POST.get("pw")
    user = authenticate(username=username, password=pw)
    if user is not None:
        request.session['username'] = user.username
        request.session['role'] = user.details.role
        messages.add_message(request, messages.SUCCESS, "You have logged in successfully.")
        return redirect('Safety:home_user_logged_in')
    else:
        messages.add_message(request, messages.ERROR, "Invalid username or password.")
        return redirect('Safety:home_user_logged_in')


def logout_user(request):
    try:
        del request.session['username']
        del request.session['role']
    except KeyError:
        pass
    return redirect('safety:home')
