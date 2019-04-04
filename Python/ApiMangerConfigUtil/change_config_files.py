import shutil


def change_file(task, src, dst):

    """This function will copy the files from given location to required location in API Manger

        Later this will replaced by templating"""

    print('Trying to configure %s' % task)
    if shutil.copyfile(src, dst):
        print('Successfully  changed %s' % task)
    else:
        print("%s changing failed!!" % task)
