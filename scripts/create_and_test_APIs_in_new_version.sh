#!/bin/bash

cd testing/bin #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~DO CHANGES FOR THIS USING pushd AND popd~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
sh jmeter.sh -n -t Scenario_003_APIM.jmx -l log.jtl

<<COMMENT
***************uncomment if needed*****************
#Show log
cat log.jtl
***************************************************
COMMENT

echo "****************************configure master-datasources**********************************"
