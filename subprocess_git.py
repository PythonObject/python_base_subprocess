# coding: utf-8
"""
subprocess 模块学习，主要用于调用git 命令行对git 仓进行操作，包括pull、push等操作，提供给一个接口使得两个代码中的
所有分支同步
"""

import subprocess
import os
import time

# bash = "ls"
# para = "-al"
# retcode = subprocess.call([bash, para])
# print "---------------------"
# print retcode
# print type(retcode)
# print "---------------------"

# 写入文件
outputfilename = 'outputlog.txt'
outputfile_object = open(outputfilename, 'ab+')
outputfile_object.write(time.strftime('%Y-%m-%d',time.localtime(time.time())))

errorfilename = 'errorlog.txt'
errorfile_object = open(errorfilename, 'ab+')
errorfile_object.write(time.strftime('%Y-%m-%d',time.localtime(time.time())))

bash = "git"
active = "push"
option = "test"
branch = "master"

# 切换路径
dir = "/home/wmm/studydata"
os.chdir(dir)

active = "clone "
para = "--bare"
url = "git@github.com:PythonObject/python_base_subprocess_test_repository.git"
command = format("" + bash + ' ' + active +' ' + '' + url)
# command = "git clone git@github.com:PythonObject/python_base_subprocess_test_repository.git"
# print command
# subprocess.call(bash, None, para, active, url)
result = subprocess.Popen(
    args=command,
    shell=True,
    stdin=None,
    stdout=outputfile_object,
    stderr=errorfile_object,
).wait()
print result
print type(result)

errorfile_object.close()
errorfile_object.close()


# 直接push到另一个remote
# bash = "git"
# active = "push"
# option = "test"
# branch = "master"
# # url = "git@github.com:PythonObject/python_base_subprocess_test_repository.git"
# retcode = subprocess.call([bash, active, option, branch])
# print retcode


