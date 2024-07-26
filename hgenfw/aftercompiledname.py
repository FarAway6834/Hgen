from csv import DictReader as csvr
from os.path import dirname as getdir
from os.path import abspath as getabs
from os import chdir as cd
from os import getcwd as pwd

o = open

def mov2thisfiledir(func):
  where = getdir(getabs(__file__))
  def core(argvs):
    back = pwd()
    cd(where)
    ret = func(argvs)
    cd(back)
    return ret
  return core

def wither(opener):

  def with_deco(func):

    def with_core(fn):
      with opener(fn) as fp:
        return func(fp)
    return with_core

  return with_deco


@wither(o)
def tsvloadscore(fp):
  yield from csvr(fp, delimiter='\t')

def tsvloads(f):
  ret = tsvloadscore(f)
  ret = (ret, next(ret))
  ret[0].close()
  return ret[1]
  
maps = mov2thisfiledir(tsvloads)('filenamemap.tsv')

class UndefinedExtErr(Exception): pass

def maper(x):
  y = x.split('.')
  z = [None, None]
  match y.pop():
    case 'myhc': z = ['', 'h']
    case 'domh': z = ['domh', 'h']
    case 'lvdomh': z = ['lv', 'domh']
    case 'iomh': z = ['includer', 'myhc']
    case 'siomh': z = ['std', 'myhc']
    case 'xiomh': z = ['unstd', 'myhc']
    case 'thmh': z = ['types', 'myhc']
    case _: raise UndefinedExtErr(f"'{x}' is not hgenfw's file")
  y.append(z.pop())
  return z.pop() + '.'.join(y)