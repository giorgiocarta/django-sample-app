from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpRequest
from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required


# from django.contrib.auth.


def register(request: HttpRequest) -> HttpResponse:
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            # username = form.cleaned_data.get('username')

            messages.success(
                request=request,
                message=f"Your account has been created! You are now able to login")
            return redirect('login')
    else:
        form = UserRegisterForm()

    return render(
        request=request,
        template_name='users/register.html',
        context={"form": form})


@login_required
def profile(request: HttpRequest) -> HttpResponse:
    if request.method == 'POST':
        """
        If this is an update
        """
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(
            request.POST,
            request.FILES,
            instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()

            username = u_form.cleaned_data.get('username')
            messages.success(
                request=request,
                message=f"Hi {username}, your account has been updated!")
            return redirect('profile')
    else:
        """
        If this is not an update
        """
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)

    context = {'u_form': u_form, 'p_form': p_form}

    return render(
        request,
        'users/profile.html',
        context=context
    )
