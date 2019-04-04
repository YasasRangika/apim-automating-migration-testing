print("Hello Yasas")






































# from shutil import copyfile
# from properties import *
#
#
# def ver2_1_0():
#     print("Trying to configure registry.xml")
#     if copyfile('../data/APIM_%S/registry.xml' % OLD_VERSION,
#                 '%s/wso2am-%s/repository/conf/registry.xml' % (APIM_HOME_PATH, OLD_VERSION)):
#         print("Successfully  configured registry.xml")
#     else:
#         print(
#             "Configuration failed, Please manually configure the /repository/conf/registry.xml file as previous version")
#
#
# def ver2_2_0():
#     print("two")
#     print("done")
#
#
# def ver2_5_0():
#     print("three")
#     print("done")
#
#
# switcher = {
#     "2.1.0": ver2_1_0,
#     "2.2.0": ver2_2_0,
#     "2.5.0": ver2_5_0
# }
#
#
# def numbers_to_strings(argument):
#     func = switcher.get(argument, "nothing")
#     return func()
#
#
# if __name__ == "__main__":
#     numbers_to_strings(OLD_VERSION)
