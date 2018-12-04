import paramiko
from django.http import HttpResponse
from django.shortcuts import render


def linsdk_manage(request):
    return render(request, "linsdk_manage.html")


def linsdk_test(request):
    if request.method == "POST":
        interface = request.POST.get("interface", "")
        algversion = request.POST.get("algversion", "")
        sdkversion = request.POST.get("sdkversion", "")

        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect('192.168.11.25', 22, 'intellif', 'introcksai', timeout=5)
        sdkdir = "/home/intellif/SDK/IFaceRecSDK/v2.1.0/rc1/"

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
            stdin, stdout, stderr = ssh.exec_command("cd " + sdkdir + " && ./run.sh >>" + sdkdir + "all.txt")
            stdout.read().decode()
            ssh.exec_command("sed -i 's/^${/#${/' " + sdkdir + "run.sh")
            sftp = ssh.open_sftp()
            relog = sftp.open(sdkdir + "all.txt")
            result = relog.read().decode()
            relog.close()
            return HttpResponse(result)
    else:
        return HttpResponse("请求方法不正确")
