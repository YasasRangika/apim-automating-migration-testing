f = open("/home/yasas/Desktop/migration-config.yaml", "r+")

newText = ""
while True:
    line = f.readline()
    if not line:
        break
    if line.count("currentVersion") > 0:
        newText += "currentVersion: \"2.5.0\" \n"
    else:
        newText += line
f.close()
f = open("/home/yasas/Desktop/migration-config.yaml", "w+")
f.write(newText)
f.close()
