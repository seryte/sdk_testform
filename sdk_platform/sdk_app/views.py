import os, time
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect


# Create your views here.

def sdk_manage(request):
    return render(request, "sdk_manage.html")


def upload(request):
    if request.method == 'POST':
        file_obj = request.FILES.get('file')
        f = open(os.path.join('upload', file_obj.name), 'wb')
        print(file_obj, type(file_obj))
        print(file_obj.name)
        for chunk in file_obj.chunks():
            f.write(chunk)
        f.close()
        return HttpResponse('OK')


def sdk_test(request):
    if request.method == "POST":
        interface = request.POST.get("interface", "")
        algversion = request.POST.get("algversion", "")
        sdkversion = request.POST.get("sdkversion", "")
        os.system("F:\\SDK\\Windows\\v2.1.2\\rc1\\run64.bat")
        if interface == "人脸检测":
            file = "F:\\SDK\\Windows\\v2.1.2\\rc1\\output\\detector_result\\log.txt"
            with open(file, "r") as f:
                return HttpResponse(f.read())
    return HttpResponse(algversion)


def linsdk_manage(request):
    return render(request, "linsdk_manage.html")
