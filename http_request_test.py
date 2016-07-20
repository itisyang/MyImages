from http_request import ffi

libname = 'ppsdk/libppsdk.dll'
lib = ffi.dlopen(libname)      # Unix: open the standard C library
#import ctypes.util         # or, try this on Windows:
#lib = ffi.dlopen(ctypes.util.find_library("c"))

bufsize=4096*5
response = ffi.new("char[]", bufsize)
print response
print len(response)
size = ffi.new("size_t *")
size[0]=bufsize
ret = lib.http_request("http://www.baidu.com", ffi.NULL, ffi.NULL, response, size)
print ret
