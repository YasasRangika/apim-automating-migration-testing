#!/bin/bash
DIR=$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )
source "$DIR/../properties.conf"

sed -i 's/.*migrationEnable.*/migrationEnable: "true"/' ../data/Identity_component_upgrade/wso2is-$is_version-migration/migration-resources/migration-config.yaml
sed -i 's/.*currentVersion.*/currentVersion: "5.3.0"/' ../data/Identity_component_upgrade/wso2is-$is_version-migration/migration-resources/migration-config.yaml
