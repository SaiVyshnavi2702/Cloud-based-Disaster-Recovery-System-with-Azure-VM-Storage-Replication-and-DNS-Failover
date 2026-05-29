from django.shortcuts import render
from django.http import HttpResponse
from .models import Register
import socket
import subprocess

def home(request):
    hostname = socket.gethostname()
    hip = subprocess.run(['curl','ifconfig.me'], stdout=subprocess.PIPE)

    regdata = f"Host name: {hostname} | Host IP: {hip.stdout}"

    if request.method == 'POST':
        data = request.POST

        Register.objects.create(
            name=data['name'],
            mailid=data['email'],
            college=data['college'],
            contact=data['no'],
            loc=data['loc']
        )

        return render(request, 'index.html', {
            'regdata': regdata,
            'data': 'Registration successful'
        })

    return render(request, 'index.html', {'regdata': regdata})