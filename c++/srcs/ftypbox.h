#ifndef FTYPBOX_H
#define FTYPBOX_H

#include "type.h"
#include "box.h"
#include "bitstream.h"
#include <vector>

class FtypBox : public Box
{
public:
    FtypBox();
    ~FtypBox();

    void ReadBox(BitStream *p_bitstream);
    void Print();

private:
    const static INT MAX_BRAND = 16;
    UINT32 m_major_brand;
    UINT32 m_minor_brand;
    UINT32 m_num_of_brand;
    // UINT32 m_compatible_brands[MAX_BRAND]; // TODO
    std::vector<UINT32> m_compatible_brands;
};

#endif