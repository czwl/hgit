import subprocess

encoding = "utf-8"

import subprocess
import sys

user = sys.argv[1]
api = f"https://api.github.com/users/{user}/repos?per_page=200"

import urllib.request, json

with urllib.request.urlopen(api) as url:
    data = json.loads(url.read().decode())
    print(json.dumps(data, indent=4, sort_keys=True))
    for r in data:
        url = r.get("ssh_url")
        subprocess.run(["git", "clone", url])
        print(url)


def git_r(args):
    if any(isinstance(el, list) for el in args):
        for cmd in args:
            subprocess.run(cmd)
    else:
        subprocess.run(args)


def git_output(args, func=None):
    rout = subprocess.check_output(args).decode(encoding)
    if func is None:
        return rout
    else:
        return func(rout)
    first = rout.splitlines()[0]
    return first
