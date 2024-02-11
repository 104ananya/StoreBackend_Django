from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

# view function is a function that takes REQUEST ---> send RESPONSE
# request : client's browser sends HTTP request to server, and server sends HTTP response to client
# it is request handler
#  it is also  called ACTION / VIEW


def say_hello(request):
    
    # it is a function that takes a request and returns an HTTP response
    # we can do anything like --- 1. pull data from database.
    # 2. manipulate data / Transform
    # 3. Send email

    # return HttpResponse("Hello World")
    
    return render(request, 'hello.html')

