import yaml

with open("/home/yasas/migration-config.yaml") as f:
    list_doc = yaml.load(f)

for migratorConfigs in list_doc:
    # if migratorConfigs["name"] == "EventPublisherMigrator":
    #     migratorConfigs["order"] = 1234;
    print(migratorConfigs)

# with open("/home/yasas/migration-config.yaml", "w") as f:
#     yaml.dump(list_doc, f)
