import os
import re, subprocess
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from threading import Thread

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
        batdir = "I:\\v2.1.2\\rc1\\"
        runbat = batdir + "run64.bat"
        interface = request.POST.get("interface", "")
        algversion = request.POST.get("algversion", "")
        sdkversion = request.POST.get("sdkversion", "")

        if interface == "人脸检测":
            modifybat(runbat, "rem call DetectorTest.exe", "call DetectorTest.exe")
            os.system(runbat)
            modifybat(runbat, "call DetectorTest.exe", "rem call DetectorTest.exe")
            file = batdir + "output\\detector_result\\log.txt"
            with open(file, "r") as f:
                return HttpResponse(f.read())
        elif interface == "特征提取":
            modifybat(runbat, "rem call ExtractorTest.exe", "call ExtractorTest.exe")
            os.system(runbat)
            modifybat(runbat, "call ExtractorTest.exe", "rem call ExtractorTest.exe")
            file = batdir + "output\\extractor_result\\log.txt"
            with open(file, "r") as f:
                return HttpResponse(f.read())
        elif interface == "1比1比对":
            modifybat(runbat, "rem call ComparerTest.exe", "call ComparerTest.exe")
            os.system(runbat)
            modifybat(runbat, "call ComparerTest.exe", "rem call ComparerTest.exe")
            file = batdir + "output\\comparer_result\\log.txt"
            with open(file, "r") as f:
                return HttpResponse(f.read())
        elif interface == "人脸搜索(1:N)":
            modifybat(runbat, "rem call SearcherTest.exe", "call SearcherTest.exe")
            os.system(runbat)
            modifybat(runbat, "call SearcherTest.exe", "rem call SearcherTest.exe")
            file = batdir + "output\\searcher_result\\log.txt"
            with open(file, "r") as f:
                return HttpResponse(f.read())
        elif interface == "人脸属性":
            modifybat(runbat, "rem call PredictorTest.exe", "call PredictorTest.exe")
            os.system(runbat)
            modifybat(runbat, "call PredictorTest.exe", "rem call PredictorTest.exe")
            file = batdir + "output\\predictor_result\\log.txt"
            with open(file, "r") as f:
                return HttpResponse(f.read())
        elif interface == "人脸抓拍":
            modifybat(runbat, "rem call CapturerTest.exe", "call CapturerTest.exe")
            os.system(runbat)
            modifybat(runbat, "call CapturerTest.exe", "rem call CapturerTest.exe")
            file = batdir + "output\\capturer_result\\log.txt"
            with open(file, "r") as f:
                return HttpResponse(f.read())
        elif interface == "人脸跟踪":
            modifybat(runbat, "rem call TrackerTest.exe", "call TrackerTest.exe")
            os.system(runbat)
            modifybat(runbat, "call TrackerTest.exe", "rem call TrackerTest.exe")
            file = batdir + "output\\tracker_result\\log.txt"
            with open(file, "r") as f:
                return HttpResponse(f.read())
        elif interface == "全部":
            modifybat(runbat, "rem call", "call")
            os.system(runbat+">>"+batdir+"all_log.txt")
            modifybat(runbat, "call", "rem call")
            file = batdir + "all_log.txt"
            with open(file, "r") as f:
                return HttpResponse(f.read())
    return HttpResponse(algversion)


def linsdk_manage(request):
    return render(request, "linsdk_manage.html")
