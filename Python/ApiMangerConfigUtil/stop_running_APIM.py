import os
import subprocess

def stopRunningServer(home, version):

    subprocess.Popen(["sh", "%s/wso2am-%s/bin/wso2server.sh" % (home, version), "stop"])
