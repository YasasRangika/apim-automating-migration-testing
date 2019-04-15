with open("/home/yasas/Videos/testing2/wso2am-2.1.0/dbscripts/apimgt/mysql5.7.sql", 'r') as my_file:
    data = my_file.read()
    para = ''
    for line in data.splitlines(True):
        if not line.startswith('--'):
            para += line
    para = para.replace('\n', ' ')
    para = para.replace('\t', ' ')
    para = para.split(';')
    for line in para:
        print("Executing Query-> {}".format(line))
