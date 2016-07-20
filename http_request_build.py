from cffi import FFI

ffibuilder = FFI()
ffibuilder.set_source("http_request", None)
ffibuilder.cdef("""
extern int http_request(const char *url, const char *header, const char *content, char *response, size_t *size);
    """)

if __name__ == "__main__":
        ffibuilder.compile(verbose=True)
