import os
import time, numpy, ctypes

_loaderpath = os.path.dirname(__file__)
libgemm = numpy.ctypeslib.load_library('libgemm.so', _loaderpath)
def dot(a, b):
    n = a.shape[0]
    c = numpy.empty((n,n))
    libgemm.NPdgemm(ctypes.c_int(n),
                    a.ctypes.data_as(ctypes.c_void_p),
                    b.ctypes.data_as(ctypes.c_void_p),
                    c.ctypes.data_as(ctypes.c_void_p))
    return c

for n in (1000, 2000, 3000):
    print('** %s **' % n)
    a = numpy.random.random((n,n))
    t1 = time.time()
    dot(a,a)
    t0, t1 = t1, time.time(); print(t1-t0)
    a.dot(a)
    t0, t1 = t1, time.time(); print(t1-t0)

