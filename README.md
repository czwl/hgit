## A tool to manage multiple projects in a single git repo.

A `monorepo` implemented with git orphan branches. 

`monorepo` useful when you have projects that are but not related enought to have their own repo.  

`hgit` works by using orphan branches each checked out in different directories..

`hgit` uses `git worktree` introduced in `git 2.5+` . Previous versions aren't supported.


## Why hgit
- Easy setup and full history preserve in monorepo. 
- Seperation of concerns with  seperate branches and directory.



## Creating a new `hgit` repo

Initalize a new git repo
```
git init
echo "# new repo" > README.md
git add README.md && git commit -m "Initial commit."
```
`hgit init --remote git@github.com:cswl/shell.git`

Add any directory as a subproject.

`hgit set <path/to/dir>`  

Import from a exisiting remote or local `.git` without losing history.  
`hgit import </path/to/dir> git URL | local path`


Then simply run `hgit set` to push it as a branch to your remote.


### Cloning 

But you can clone an already made `hgit` repo with 
```
hgit clone url-to-repo
```


### trees managing.

Manage directory trees with `hgit tree`
`hgit tree` runs `git worktree` with added commands and mono-repo recongition

