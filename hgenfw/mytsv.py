from csv import DictWriter as csvw
from os.path import splitext as s
o = open
w = lambda f : o(f, 'w')

def wither(opener):

  def with_deco(func):

    def with_core(fn):
      with opener(fn) as fp:
        return func(fp)
    return with_core
  
  return with_deco

@wither(o)
def kidy_parser(fp):
  for i in fp.readlines():
    j = i.split('\t')
    yield (j.pop(0), j.pop())

def MyTsvDoning(f, **x):
  ks = x.keys()
  @wither(w)
  def core(fp):
    fp2 = csvw(fp, fieldnames=ks, delimiter='\t')
    fp2.writeheader()
    fp2.writerow(x)
  return core(f)

def MyTscCompile(f):
  fn, ext = s(f)
  assert ext != 'mytsv', f'not mytsv {f}'
  return MyTsvDoning(f'{fn}.tsv', kidy_parser(f))