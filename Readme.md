# Adapt subwcrev to git-svn

If you are in the unfortunate situation that your build process depends on
subwcrev (a Tortoise SVN commandline tool) and you want to use git-svn, this is
the solution.
Since subwcrev does not work on git-svn repositories, subwcrev.py gets the revision using
the git commandline-tools. For the moment it only replaces $WCREV$, since this is all
I need.
If the git tools don't succeed, subwcrev.py falls back to the original subwcrev tool,
so it can still be used on standard subversion repos.

## Installation
The original subwcrev has to be renamed to subwcrev_orig.exe.

Build subwcrev.exe with
```
C:\Python34\python.exe .\setup.py py2exe
cp .\dist\* 'C:\Program Files\TortoiseSVN\bin\'
```

py2exe only works with python version <= 3.4
Maybe there is a better replacement but I didn't care yet.
