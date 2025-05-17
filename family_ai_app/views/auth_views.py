from django.shortcuts import render, redirect
from allauth.account.views import SignupView
from django.contrib.auth import logout

def home(request):
    return render(request, 'family_ai/home.html')

def alerts(request):
    return render(request, 'family_ai/alerts.html')

class CustomSignupView(SignupView):
    def form_valid(self, form):
        response = super().form_valid(form)
        logout(self.request)
        return redirect('/accounts/login/')