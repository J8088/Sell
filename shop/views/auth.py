from django.views.generic import View
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect


class Login(View):
    TEMPLATE_NAME = 'login.html'

    def post(self, request):
        username = request.POST['username']
        password = request.POST['password']
        u = authenticate(username=username, password=password)
        if u and u.is_active:
            login(request, u)
            redirect_url = request.GET.get('next') or '/'
            return redirect(redirect_url)
        else:
            msg = 'Invalid credentials or inactive account'
        context = {'msg': msg}
        return render(request, self.TEMPLATE_NAME, context)

    def get(self, request):
        return render(request, self.TEMPLATE_NAME)
