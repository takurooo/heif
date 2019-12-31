#ifndef UTIL_H
#define UTIL_H

#include <cassert>
#include "type.h"

void UtilAssert(bool expr, const CHAR *msg, const CHAR *file, const CHAR *func, UINT32 line);

#define UTIL_PRINT                    \
    printf("[HEIF] [%s] ", __FILE__); \
    printf
#define UTIL_ERR_PRINT                                         \
    printf("[HEIF]ERR file:%s line:%d  ", __FILE__, __LINE__); \
    printf

#define UTIL_ASSERT(expr, msg) UtilAssert(expr, msg, __FILE__, __FUNCTION__, __LINE__)
#endif