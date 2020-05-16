#!/usr/bin/env python3
#
# Copyright (C) 2020 Czwl Cd
# Website: https://github.com/czwl
#
# SPDX-License-Identifier: Apache-2.0
#


import subprocess
import os
import re

from pathlib import Path


from config import read_config, write_config
from traverse import find_hgconf
from git import Repo


default_hgroot_name = ".hgroot"


def get_hgroot_repo(path):
    return Repo(path)


def clone_hgit_repo(remote_url):
    cwd = Path.cwd()
    print("Setting up {}", remote_url)
    write_config(remote_url)
    hgroot_path = cwd.joinpath(default_hgroot_name)
    subprocess.run(["git", "clone", "--single-branch", remote_url, ".hgroot"])
    os.chdir(hgroot_path)


def setup_git_branch():
    hgit_conf = find_hgconf(cwd)
    hgit_root = hgit_conf.parent
    hgit_branch = str(cwd.relative_to(hgit_root))
    remote = read_config(hgit_conf)

    subprocess.run(["git", "remote", "add", "origin", remote])
    subprocess.run(["git", "checkout", "-b", hgit_branch])
    subprocess.run(["git", "push", "-u", "origin", hgit_branch])


def to_temp_name(name):
    return f"XSX_tmp_{name}"


def checkout_temp_branch(name):
    return ["git", "checkout", "-b", name, f"XXX_temp_{name}/master"]


def add_temp_remote(name, path):
    return [
        ["git", "remote", "add", f"XXX_temp_{name}", path],
        ["git", "remote", "update"],
    ]


def push_current_branch():
    cur_branch = git_output(["git", "rev-parse", "--abbrev-ref", "HEAD"])
    return ["git", "push "]
