#ifndef BOXREADER_H
#define BOXREADER_H

#include "type.h"
#include "bitstream.h"
#include "ftypbox.h"
#include "metabox.h"
#include "mdatbox.h"

class BoxReader
{
public:
    BoxReader(CHAR *p_buffer, UINT64 file_size);
    ~BoxReader();
    void ReadBox();
    void ReadBoxes();

private:
    BitStream m_bitstream;
    void ReadHeader(UINT32 &BoxType, UINT32 &BoxSize);
    FtypBox m_ftyp;
    MetaBox m_meta;
    MdatBox m_mdat;
};

#endif