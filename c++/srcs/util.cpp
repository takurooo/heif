// -----------------------------------------
// include
// -----------------------------------------
#include <iostream>
#include "util.h"
// -----------------------------------------
// define
// -----------------------------------------

// -----------------------------------------
// global value
// -----------------------------------------

// -----------------------------------------
// class/function
// -----------------------------------------
void UtilAssert(bool expr, const CHAR *msg, const CHAR *file, const CHAR *func, UINT32 line)
{
    if (!expr)
    {
        UTIL_PRINT("ASSERT File:%s, Func:%s, Line:%lu,  %s\n", file, func, line, msg);
        assert(expr);
    }
}