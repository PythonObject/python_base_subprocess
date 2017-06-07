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


bash = "git"
active = "push"
option = "test"
branch = "master"

# 切换路径
dir = "/home/wmm/studydata"
os.chdir(dir)

# 端口自测试
# subprocess._demo_posix()

active = "clone "
para = "--bare"
url = "git@github.com:PythonObject/python_base_subprocess_test_repository.git"
command = format("" + bash + ' ' + active +' ' + '' + url)
pro = subprocess.Popen(
    args=command,
    shell=True,
    stdin=None,
    stderr=subprocess.PIPE,
    stdout=subprocess.PIPE
)

# poll 用来检查新创建的进程是否结束
while pro.poll() == None:
    print pro.stdout.readline()

print "return code:"
print pro.returncode
print "error:"
print pro.stderr.readline()
print "output:"
print pro.stdout.readline()

# pro.kill()



# 直接push到另一个remote
# bash = "git"
# active = "push"
# option = "test"
# branch = "master"
# # url = "git@github.com:PythonObject/python_base_subprocess_test_repository.git"
# retcode = subprocess.call([bash, active, option, branch])
# print retcode


