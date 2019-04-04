#!/bin/bash

set -e
location=$1

if [[ -z $location ]]; then
  echo 'Usage: ./apim200_to_apim210_gateway_artifact_migrator.sh <location of gateway artifacts>'
  exit 1
fi

echo gateway artifact location: "$(cd "$(dirname "$location")"; pwd -P)"

pushd $location > /dev/null

echo 'starting gateway artifact migration...'

find . -name '*.xml' -print0 | xargs -0 sed -i -e 's/org.wso2.carbon.mediator.cache.digest.DOMHASHGenerator/org.wso2.carbon.mediator.cache.digest.REQUESTHASHGenerator/'
find . -name '*.xml' -print0 | xargs -0 sed -i -e 's/org.wso2.caching.digest.REQUESTHASHGenerator/org.wso2.carbon.mediator.cache.digest.REQUESTHASHGenerator/'

popd > /dev/null

echo 'migration completed.'
