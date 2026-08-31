from django.http import JsonResponse
from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate,login,logout
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.contrib.auth.models import User
from .serializers.serializers import UserSerializer, RegisterSerializer


@api_view(['GET'])
def user_list(request):
    users = User.objects.all()
    serializer = UserSerializer(users, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def register(request):
    serializer = RegisterSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()
        return Response(
            {
            "message": 'User created successfully',
            "user" : serializer.data
            },
            status=201
        )
    return Response(serializer.errors,status=400)

def LOGIN_PAGE(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request,username=username,password=password)

        if user is not None:
            login(request, user)
            return redirect('dashboard')
        else:
            return render(request,'accounts/login.html',{'error':'Login Unsuccessful. Please check username and password'})
    return render(request,'accounts/login.html')

@login_required
def DASHBORD(request):
    return render(request,'accounts/dashboard.html')

@login_required
def PROFILE(request):
    return render(request,'accounts/profile.html')

@login_required
def ABOUT(request):
    return render(request,'accounts/about.html')

def LOGOUT(request):
    logout(request)
    return redirect('login')