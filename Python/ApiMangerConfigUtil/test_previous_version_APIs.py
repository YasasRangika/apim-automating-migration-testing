import os

def testPreviousVersionData():
    os.system('sh ../testing/bin/jmeter.sh -n -t ../testing/bin/Scenario_002_APIM.jmx -l log.jtl')
