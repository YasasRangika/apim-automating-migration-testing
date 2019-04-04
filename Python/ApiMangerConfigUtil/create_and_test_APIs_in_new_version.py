import os


def createNTestInNewAPIM():
    os.system('sh ../testing/bin/jmeter.sh -n -t ../testing/bin/Scenario_003_APIM.jmx -l log.jtl')
