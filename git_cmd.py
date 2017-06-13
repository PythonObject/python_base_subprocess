# coding: utf-8

import subprocess
import os


class git_log():
    """git log"""


class git_cmd():
    """git command"""
    def __init__(self, path, repository_url):
        # 初始化数据
        self.url = repository_url
        self.output = ''
        self.error = ''
        self.command = ''
        self.remotes = []
        self.branches = {}
        try:
            os.chdir(path)
        except Exception, error:
            print error

        # cwd 参数只有windows系统下才生效
        self.cmd = subprocess.Popen(args="git --version",
                                    shell=True,
                                    stdin=subprocess.PIPE,
                                    stdout=subprocess.PIPE,
                                    stderr=subprocess.PIPE,
                                    cwd=path)
        self._check_result()

    def _check_result(self):
        """check last cmd"""
        # 检查上一条命令是否结束
        self.output, self.error = self.cmd.communicate(input=None)

    def _run_cmd(self):
        """run cmd and return output and error"""
        # 运行git命令并返回输出和错误码
        self.cmd.communicate(stdin=self.command)
        self._check_result()
        return self.output, self.error

    def clone(self):
        """git clone """
        # 拉取远端仓代码到本地
        # git clone [--template=<template_directory>]
        # [-l] [-s] [--no-hardlinks] [-q] [-n] [--bare] [--mirror]
        # [-o <name>] [-b <name>] [-u <upload-pack>] [--reference <repository>]
        # [--dissociate] [--separate-git-dir <git dir>]
        # [--depth <depth>] [--[no-]single-branch]
        # [--recursive | --recurse-submodules] [--] <repository>
        # [<directory>]
        self.command = "git clone " + self.url
        return self._run_cmd()

    def branch_update(self):
        """git branch """
        # 更新分支字典
        self.command = "git branch -r"
        self._run_cmd()
        self.remote_update()
        # 按照'\n'分割字符串
        self.output.split('\n')
        for remote in self.remotes:
            # 给一个远端添加一个key,其数据为一个列表
            self.branches[remote] = []
            for branch in self.output[0, -1]:
                if remote in branch:
                    # 在返回的分支字符串中删除远端和/
                    branch.split(remote + '/')
                    # 添加分支到列表
                    self.branches[remote].append(branch)
        return self.output, self.error

    def remote_update(self):
        """get remote """
        # 获取远端列表
        self.command = "git remote "
        self._run_cmd()
        remotes = self.output.split('\n')
        # 清空原有列表
        for index in range(len(self.remotes)):
            self.remotes.pop()
        for remote in remotes:
            self.remotes.append(remote)
        return self.output, self.error

    def add_remote(self, name, remote_url):
        """add remote """
        # 添加远端
        self.command = "git remote add " + name + remote_url
        return self._run_cmd()

    def pull_current_branch(self, remote):
        """git pull """
        # 从指定远端拉取当前分支
        # git pull [options] [<repository> [<refspec>...]]
        self.command = "git pull " + remote
        return self._run_cmd()

    def pull_all_branch(self, remote):
        """pull all branch"""
        # 从指定远端拉取所有分支代码
        # 0. 记录当前分支
        # 1. 更新所有远端和分支
        # 2. 循环切换分支和拉取分支
        # 3. 切回原分支
        # 待编辑

        return self._run_cmd()





