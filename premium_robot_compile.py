# -*- coding: utf-8 -*-

"""

Byte-compile a single source file, please refer to https://docs.python.org/zh-cn/3.8/library/py_compile.html.
And compile all source files in a directory tree, refer to https://docs.python.org/zh-cn/3.8/library/compileall.html.

"""

# import py_compile
import compileall


# py_compile.compile('/Users/syx/Work/premium_robot/wayang_common/etcd_client.py')
compileall.compile_dir(r'/Users/syx/Work/premium_robot', maxlevels=2)