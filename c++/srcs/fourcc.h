#ifndef FOURCC_H
#define FOURCC_H

#include "type.h"
#define TYPE(c1, c2, c3, c4) (static_cast<UINT32>((c1) << 24) | \
                              static_cast<UINT32>((c2) << 16) | \
                              static_cast<UINT32>((c3) << 8) |  \
                              static_cast<UINT32>((c4) << 0))

namespace FOURCC
{
enum
{
    UUID = TYPE('u', 'u', 'i', 'd'),
    FTYP = TYPE('f', 't', 'y', 'p'),
    META = TYPE('m', 'e', 't', 'a'),
    HDLR = TYPE('h', 'd', 'l', 'r'),
    DINF = TYPE('d', 'i', 'n', 'f'),
    DREF = TYPE('d', 'r', 'e', 'f'),
    PITM = TYPE('p', 'i', 't', 'm'),
    ILOC = TYPE('i', 'l', 'o', 'c'),
    IINF = TYPE('i', 'i', 'n', 'f'),
    INFE = TYPE('i', 'n', 'f', 'e'),
    IREF = TYPE('i', 'r', 'e', 'f'),
    IPRP = TYPE('i', 'p', 'r', 'p'),
    IDAT = TYPE('i', 'd', 'a', 't'),
    MDAT = TYPE('m', 'd', 'a', 't'),

    MIME = TYPE('m', 'i', 'm', 'e'),
    URI = TYPE('u', 'r', 'i', ' '),
};
};

#endif