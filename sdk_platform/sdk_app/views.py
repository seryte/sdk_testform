import os
import re
import subprocess
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
        for chunk in file_obj.chunks():
            f.write(chunk)
        f.close()
        return HttpResponse('OK')


# 工具-修改批处理文件
def modifybat(file, old_str, new_str):
    with open(file, "r", encoding="utf-8") as f1, \
            open("%s.bak" % file, "w", encoding="utf-8") as f2:
        new_str.replace(" ", "", 1)
        for line in f1:
            f2.write(re.sub(old_str, new_str, line))
    os.remove(file)
    os.rename("%s.bak" % file, file)


def sdk_test(request):
    if request.method == "POST":
        batdir = "F:\\SDK\\Windows\\v2.1.2\\rc1\\"
        runbat = batdir + "run64.bat"
        interface = request.POST.get("interface", "")
        algversion = request.POST.get("algversion", "")
        sdkversion = request.POST.get("sdkversion", "")

        if interface == "人脸检测":
            modifybat(runbat, "rem call %dir_detector%", "call %dir_detector%")
            os.system(runbat)
            modifybat(runbat, "call %dir_detector%", "rem call %dir_detector%")
            file = batdir + "output\\detector_result\\log.txt"
            with open(file, "r") as f:
                return HttpResponse(f.read())
        elif interface == "特征提取":
            modifybat(runbat, "rem call %dir_extractor%", "call %dir_extractor%")
            os.system(runbat)
            modifybat(runbat, "call %dir_extractor%", "rem call %dir_extractor%")
            file = batdir + "output\\extractor_result\\log.txt"
            with open(file, "r") as f:
                return HttpResponse(f.read())
        elif interface == "1比1比对":
            modifybat(runbat, "rem call %dir_comparer%", "call %dir_comparer%")
            os.system(runbat)
            modifybat(runbat, "call %dir_comparer%", "rem call %dir_comparer%")
            file = batdir + "output\\comparer_result\\log.txt"
            with open(file, "r") as f:
                return HttpResponse(f.read())
        elif interface == "人脸搜索(1:N)":
            modifybat(runbat, "rem call %dir_searcher%", "call %dir_searcher%")
            os.system(runbat)
            modifybat(runbat, "call %dir_searcher%", "rem call %dir_searcher%")
            file = batdir + "output\\searcher_result\\log.txt"
            with open(file, "r") as f:
                return HttpResponse(f.read())
        elif interface == "人脸属性":
            modifybat(runbat, "rem call %dir_predictor%", "call %dir_predictor%")
            os.system(runbat)
            modifybat(runbat, "call %dir_predictor%", "rem call %dir_predictor%")
            file = batdir + "output\\predictor_result\\log.txt"
            with open(file, "r") as f:
                return HttpResponse(f.read())
        elif interface == "人脸抓拍":
            modifybat(runbat, "rem call %dir_capturer%", "call %dir_capturer%")
            os.system(runbat)
            modifybat(runbat, "call %dir_capturer%", "rem call %dir_capturer%")
            file = batdir + "output\\capturer_result\\log.txt"
            with open(file, "r") as f:
                return HttpResponse(f.read())
        elif interface == "人脸跟踪":
            modifybat(runbat, "rem call %dir_tracker%", "call %dir_tracker%")
            os.system(runbat)
            modifybat(runbat, "call %dir_tracker%", "rem call %dir_tracker%")
            file = batdir + "output\\tracker_result\\log.txt"
            with open(file, "r") as f:
                return HttpResponse(f.read())
        elif interface == "全部":
            modifybat(runbat, "rem call %dir_", "call %dir_")
            os.system(runbat + ">>" + batdir + "all_log.txt")
            modifybat(runbat, "call %dir_", "rem call %dir_")
            file = batdir + "all_log.txt"
            with open(file, "r") as f:
                return HttpResponse(f.read())
    return HttpResponse(algversion)


def linsdk_manage(request):
    return render(request, "linsdk_manage.html")
