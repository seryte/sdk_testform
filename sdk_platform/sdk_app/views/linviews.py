import os
import paramiko
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render

sdkdir = "/home/intellif/SDK/IFaceRecSDK/v2.1.0/rc1/"
outdir = sdkdir + "output/"
server = "192.168.11.25"
port = 22
username = "intellif"
password = "introcksai"


@login_required
def linsdk_manage(request):
    return render(request, "linsdk_manage.html")


@login_required
def linsdk_test(request):
    if request.method == "POST":
        interface = request.POST.get("interface", "")
        algversion = request.POST.get("algversion", "")
        sdkversion = request.POST.get("sdkversion", "")

        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(server, port, username, password, timeout=5)

        if interface == "detector":
            ssh.exec_command(
                "sed -i 's/^#${detector}/${detector}/' " + sdkdir + "run.sh")
            stdin, stdout, stderr = ssh.exec_command("cd " + sdkdir + " && ./run.sh")
            stdout.read().decode()
            ssh.exec_command("sed -i 's/^${detector}/#${detector}/' " + sdkdir + "run.sh")
            sftp = ssh.open_sftp()
            relog = sftp.open(sdkdir + "output/detector_result/log.txt")
            result = relog.read().decode()
            relog.close()
            return HttpResponse(result)

        elif interface == "extractor":
            ssh.exec_command(
                "sed -i 's/^#${extractor}/${extractor}/' " + sdkdir + "run.sh")
            stdin, stdout, stderr = ssh.exec_command("cd " + sdkdir + " && ./run.sh")
            stdout.read().decode()
            ssh.exec_command("sed -i 's/^${extractor}/#${extractor}/' " + sdkdir + "run.sh")
            sftp = ssh.open_sftp()
            relog = sftp.open(sdkdir + "output/extractor_result/log.txt")
            result = relog.read().decode()
            relog.close()
            return HttpResponse(result)

        elif interface == "comparer":
            ssh.exec_command(
                "sed -i 's/^#${comparer}/${comparer}/' " + sdkdir + "run.sh")
            stdin, stdout, stderr = ssh.exec_command("cd " + sdkdir + " && ./run.sh")
            stdout.read().decode()
            ssh.exec_command("sed -i 's/^${comparer}/#${comparer}/' " + sdkdir + "run.sh")
            sftp = ssh.open_sftp()
            relog = sftp.open(sdkdir + "output/comparer_result/log.txt")
            result = relog.read().decode()
            relog.close()
            return HttpResponse(result)

        elif interface == "searcher":
            ssh.exec_command(
                "sed -i 's/^#${searcher}/${searcher}/' " + sdkdir + "run.sh")
            stdin, stdout, stderr = ssh.exec_command("cd " + sdkdir + " && ./run.sh")
            stdout.read().decode()
            ssh.exec_command("sed -i 's/^${searcher}/#${searcher}/' " + sdkdir + "run.sh")
            sftp = ssh.open_sftp()
            relog = sftp.open(sdkdir + "output/searcher_result/log.txt")
            result = relog.read().decode()
            relog.close()
            return HttpResponse(result)

        elif interface == "predictor":
            ssh.exec_command(
                "sed -i 's/^#${predictor}/${predictor}/' " + sdkdir + "run.sh")
            stdin, stdout, stderr = ssh.exec_command("cd " + sdkdir + " && ./run.sh")
            stdout.read().decode()
            ssh.exec_command("sed -i 's/^${predictor}/#${predictor}/' " + sdkdir + "run.sh")
            sftp = ssh.open_sftp()
            relog = sftp.open(sdkdir + "output/predictor_result/log.txt")
            result = relog.read().decode()
            relog.close()
            return HttpResponse(result)

        elif interface == "capturer":
            ssh.exec_command(
                "sed -i 's/^#${capturer}/${capturer}/' " + sdkdir + "run.sh")
            stdin, stdout, stderr = ssh.exec_command("cd " + sdkdir + " && ./run.sh")
            stdout.read().decode()
            ssh.exec_command("sed -i 's/^${capturer}/#${capturer}/' " + sdkdir + "run.sh")
            sftp = ssh.open_sftp()
            relog = sftp.open(sdkdir + "output/capturer_result/log.txt")
            result = relog.read().decode()
            relog.close()
            return HttpResponse(result)

        elif interface == "tracker":
            ssh.exec_command(
                "sed -i 's/^#${tracker}/${tracker}/' " + sdkdir + "run.sh")
            stdin, stdout, stderr = ssh.exec_command("cd " + sdkdir + " && ./run.sh")
            stdout.read().decode()
            ssh.exec_command("sed -i 's/^${tracker}/#${tracker}/' " + sdkdir + "run.sh")
            sftp = ssh.open_sftp()
            relog = sftp.open(sdkdir + "output/tracker_result/log.txt")
            result = relog.read().decode()
            relog.close()
            return HttpResponse(result)

        elif interface == "select_all":
            ssh.exec_command(
                "sed -i 's/^#${/${/' " + sdkdir + "run.sh")
            stdin, stdout, stderr = ssh.exec_command("cd " + sdkdir + " && ./run.sh")
            stdout.read().decode()
            ssh.exec_command(
                "cat " + outdir + "detector_result/log.txt " + outdir + "comparer_result/log.txt " + outdir + "searcher_result/log.txt " + outdir + "extractor_result/log.txt " + outdir + "predictor_result/log.txt " + outdir + "capturer_result/log.txt " + outdir + "tracker_result/log.txt >" + sdkdir + "all_result.txt")
            ssh.exec_command("sed -i 's/^${/#${/' " + sdkdir + "run.sh")
            sftp = ssh.open_sftp()
            relog = sftp.open(sdkdir + "all_result.txt")
            result = relog.read().decode()
            relog.close()
            return HttpResponse(result)
    else:
        return HttpResponse("请求方法不正确")


def linupload(request):
    if request.method == 'POST':
        # 先上传到本地，再上传到服务器
        file_obj = request.FILES.get('file')
        f = open(os.path.join('linupload', file_obj.name), 'wb')
        print(file_obj, type(file_obj))
        for chunk in file_obj.chunks():
            f.write(chunk)
        f.close()

        t = paramiko.Transport((server, port))
        t.connect(username=username, password=password)
        sftp = paramiko.SFTPClient.from_transport(t)
        for i in os.listdir("linupload"):
            sftp.put(os.path.join("linupload", i), os.path.join(sdkdir + "tpcase/", i))
        return HttpResponse('OK')
