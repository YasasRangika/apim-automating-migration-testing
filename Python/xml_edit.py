import xml.etree.ElementTree as ET


def edit(path, key, value):
    tree = ET.parse(path)
    root = tree.getroot()
    i = 0

    for rank in root.iter(key):
        if i < 2:
            if isinstance(value, list):
                rank.text = value[i]
            else:
                rank.text = value
        i += 1

    tree.write(path)


edit('/home/yasas/master-datasources.xml', 'username', ['test1','test2'])
