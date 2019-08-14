import subprocess
import os


def runJmeter(script):

    os.system('sh ../testing/bin/jmeter.sh -n -t ../testing/scripts/%s.jmx -l log.jtl' % script)

    # sp = subprocess.Popen(["sh", "../testing/bin/jmeter.sh", "-n", "-t", "../testing/bin/rolesAndUsersCreation.jmx"],
    #                  shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    # out, err = sp.communicate()
    # if out:
    #     print("standard output of subprocess:")
    #     print(out)
    # if err:
    #     print("standard error of subprocess:")
    #     print(err)
    # print("returncode of subprocess:")
    # print(sp.returncode)
