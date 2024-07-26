__version__ = '0.0.1'

__all__ = ['hfilegen.py', 'myhd4pyd.py', 'aftercompiledname.py', 'mytsv.py']

from os.path import isfile as isf
p = [isf('filenamemap.tsv'), isf('modlists.tsv')]
del isf
if not (isf(p[0] or p[1]):
  from shutil import run as r
  from os.path import dirname as getdir
  from os.path import abspath as getabs
  from os import chdir as cd
  from os import getcwd as pwd
  back = pwd()
  cd(getdir(getabs(__file__)))
  del getdir
  del getabs
  del pwd
  def s(x, logs = True):
    y = r(x, shell = True)
    if logs: print(y)
    return y
  from mytsv import MyTsvCompile as mtcp
  if p.pop(): mtcp('modlists.mytsv')
  if p.pop(): mtcp('filenamemap.mytsv')
  del mtcp
  del s
  del p
  cd(back)
  del cd
  del back
else:
  del p