pass
'''

many declaration needs, so we use this lib

ex) * in tempyd.cpp *
/*

//[CYF RE-DEC ZONE]
"cmdfst"         //DECLAR
"cyf"            //header's FUNC RE-DECLAR
"definedMethod"  //src places
"cmdlst"         //DECLAR
"initerMethod"   //PYD_CORE_INITER

* in header *
HFcyfHEADER   //CYF METHOD HEADER
HFcmdlstV     //cmdlst's Value
HFcmdlstITEM  //that value arr's item

LHFcore
LHFProt

*/

#include "pydlibs.h"
#include "tempyd.h"

cmdfst

cyf(f) //cf
cyf(F) //cF

definedMethod

cmdlst(exportsMethod)
initerMethod

[FORM]

#include "pydlibs.h"
#include "[filename].h"

cmdfst

cyf([src])
...

definedMethod

cmdlst(exportsMethod)
initerMethod

tempyd.myhc
[HEADER-SRC]
#define initerMethod [SRC A]
#define defineMethod exportsMethod = HFcmdlstV([Newline-'\\'ed SrcB])

[BY-MYHP]

```
[FUNC]
{[SRC]} //type, value => will compiled main-file's value. (Value = SRCB)

[INIT]    //DEPRECATE : err4design => delete it ; libname needs :)
{[SrcA]}  //DEPRECATE : err4design => delete it ; libname needs :)

[MAIN]
{[HEADER]}

[MYHDIR] //option (if Exist -> myhp inserted here.)
{[MYHDIR-SRC]} //value
```

the form and MYHP is fixed type.
`[~]` can be `$=====$ [ AND ] $=====$`

MyHP.py will manage it.

 # ==== # [ # about lib # ] # ===== #

 === # [pydlibs.myhd] ===

[pydlib.xiomh]
Python.h

[deflibs.domh]
STRINGIFY(x) #x
CONCAT(a, b) a##b

[pydlibsLvA.lvdomh]
PyObj PyObject
PyErrDeclars static PyObj *ErrorObject
ExportsCyF PyMethodDefd
CyFExportsValue(...) {__VA_ARGS__, {NULL, NULL}};
CyFExports struct ExportsCyF methods[] =
CyFItem(types, method) {STRINGIFY(method), method, types}
CyProt(func) PyObjectPtr func(PyObject *self, PyObject *args)
staticCyFuncHeads(func) static CyProt(func)
staticCyFuncSrc(func) {return CONCAT(func, (&self, &args))}
staticCyFunc(func) staticCyFuncHeads(func) staticCyFunc(CONCAT(c, func))
PydIniterDeclarHeads(libname) void CONCAT(CONCAT(init, libname), ())
IniterSrc(libname) {PyObj* m; m = Py_InitModule(STRINGIFY(libname), methods); ErrorObject = Py_BuildValue("s", "error");}
PydIniterDeclar(libname) PydIniterDeclarHeads(libname) IniterSrc(libname)
cmdfst PyErrDeclars
cmdlst CyFExports
cyf staticCyFunc
HFcyfHEADER CyProt
HFcmdlstV CyFExportsValue
HFcmdlstITEM CyFItem
LHFcore PyIniterDeclar
LHFProt PydIniterDeclarHeads

[pydlibsLvA.thmh]
PyObj* PyObjPtr
PyObjPtr *CyFunc(PyObj *self, PyObj *args)
void *pydinitf()

[pydlibs.xiomh.core]
pydlib.xiomh
deflibs.domh
pydlibsLvA.lvdomh
pydlibsLvA.thmh

[pydlibs.xiomh]
includerunstdpydlib.h
domhdeflibs.h
domhlvpydlibsLvA.h
typespydlibsLvA.h

[pydlibs.h]
#include "includerunstdpydlibs.h"

[hfilegener.py]
#make includerunstdpydlibs.h
from fgenfw.hfilegen import righttypemethods as F
from fgenfw.aftercompiledname import mapers as A
from os import listdir as l
f = l()
r = lambda x : f.remove(x)
(r('hfilegener.py'), r('pydlibs.xiomh.core'))
for i in f:
  F(f)(f)
  i = A(i)
  if not i.endswith('.h'): f.append(i)

======================================

MYHP-AType    //$=====$ [AND] $=====$
MYHP-Basic    //Basic
MYHP-Compiled //Like-MYPD but setup.py is exist.

[warning : MYHP is run on github repo, private repo is suggested.]

# setup.py
from distutils.core import setup, Extension

setup(name = "{cpp file name}",
  version = "{version}",
  description = "{readme-md description}",
  author = "{gh username}",
  author_email = "{gh email}",
  url = "{gh repo}",
  ext_modules = [Extension("{cpp file name}", ["{cpp file name : real}"])]
)

+++++++++++++++++++++++++++++++++++++++++++++++++

ExtendedMyHP

`EMHPort SET` : setting EMHPort CMD
`EMHPort` : EMHPort + registering functions on a list (up)

'''
