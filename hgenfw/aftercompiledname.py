
from csv import DictReader as csvr

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
  
map = tsvloadscore('filenamemap.tsv')