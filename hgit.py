#!/usr/bin/env python3
#
# Copyright (C) 2020 Czwl Cd
# Website: https://github.com/czwl
#
# SPDX-License-Identifier: Apache-2.0
#


from docopt import docopt
from pathlib import Path

from git import Repo
from git.refs import Reference

import hutils


def cli():
    """
    hgit - A tool to manage monorepo as git branches.
    
    Usage: 
    hgit init
    hgit set DIR
    hgit import DIR PATH 
    hgit push BRANCH
    hgit tree [-p | --populate] [ -u | --upstream ] [-a | --add SUBPROJECT]
    hgit --debug [ -s SHELL ]  [-pe] [USER]
    hgit -h | --help | --version 
        
    Options:
    --debug      Output debugging information to stderr.
    -h --help    Show this screen.
    --version    Show version.

    """
    args = docopt(cli.__doc__)
    cwd = Path.cwd()
    if args.get("init"):
        pass
    if args.get("import"):
        repo = hutils.get_hgroot_repo(cwd)
        git = repo.git
        nbranch = args.get("DIR")
        lpath = args.get("PATH")
        full_path = Path(lpath).resolve()
        git.remote(["add", f"XHG_temp_{nbranch}", full_path])
        git.remote("update")
        git.checkout(["-b", nbranch, f"XHG_temp_{nbranch}/master"])
        print("Checked out", nbranch, full_path)

    if args.get("push"):
        nbranch = args.get("BRANCH")
        if nbranch == ".":

            repo = hutils.get_hgroot_repo(cwd)
            git = repo.git
            cur_branch = repo.active_branch.name
            print(f"Pushing sub-project as {cur_branch}")
            git.push(["origin", f"{cur_branch}:{cur_branch}"])

    if args.get("tree"):
        cwd = Path.cwd()
        projects = cwd / "projects"
        repo = Repo(cwd)
        git = repo.git
        remote_name = "origin"
        remote = repo.remotes[remote_name]
        remote_refs = remote.refs

        def filterbyvalue(seq):
            for el in seq:
                if not (el.remote_head == "HEAD" or el.remote_head == "master"):
                    yield el

        remote_heads = filterbyvalue(remote_refs)
        if args.get("--add") or args.get("-a"):
            nbranch = args.get("SUBPROJECT")
            print(nbranch, projects / nbranch)
            # git.worktree(["add", "-b", nbranch, projects / nbranch, commit])
        if args.get("--populate") or args.get("-p"):
            for r in remote_heads:
                try:
                    name = r.remote_head
                    commit = r.commit
                    git.worktree(["add", "-b", name, projects / name, commit])
                    print(name, commit)
                except Exception as e:
                    raise e
                    pass
        if args.get("--upstream") or args.get("-u"):
            for r in remote_heads:
                try:
                    name = r.remote_head
                    origin_ref = f"{remote_name}/{name}"
                    git.branch(["-u", origin_ref, name])
                    print(name, origin_ref)
                except Exception as e:
                    pass

    pass
