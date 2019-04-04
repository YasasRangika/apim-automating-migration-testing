import subprocess


def runAPIM(home, version):
    subprocess.Popen(["gnome-terminal","-e","%s/wso2am-%s/bin/wso2server.sh" % (home, version)])

