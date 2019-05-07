import subprocess
import os


def runAPIM(home, version):
    subprocess.Popen(["gnome-terminal", "-e", "%s/wso2am-%s/bin/wso2server.sh" % (home, version)])
#     os.system("gnome-terminal -e /home/yasas/Videos/testing2/wso2am-2.1.0/bin/wso2server.sh")
# subprocess.Popen(["gnome-terminal", "-e", "/home/yasas/Videos/testing2/wso2am-2.1.0/bin/wso2server.sh"])
