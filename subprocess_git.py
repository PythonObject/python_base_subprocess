# coding: utf-8
"""
subprocess 模块学习，主要用于调用git 命令行对git 仓进行操作，包括pull、push等操作，提供给一个接口使得两个代码中的
所有分支同步
"""

import subprocess
import os

bash = "ls"
para = "-al"
retcode = subprocess.call([bash, para])
print "---------------------"
print retcode
print type(retcode)
print "---------------------"

# 切换路径
dir = "/home/wmm/studydata"
os.chdir(dir)
print os.getcwd()

bash = "git"
active = "push"
option = "test"
branch = "master"
# url = "git@github.com:PythonObject/python_base_subprocess_test_repository.git"
retcode = subprocess.call([bash, active, option, branch])
print retcode

