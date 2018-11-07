from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect


# Create your views here.

def sdk_manage(request):
    return render(request, "sdk_manage.html")


def sdk_test(request):
    if request.method == "POST":
        interface = request.POST.get("interface", "")
        algversion = request.POST.get("algversion", "")
        sdkversion = request.POST.get("sdkversion", "")
    return HttpResponse(interface)
