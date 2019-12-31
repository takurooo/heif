// -----------------------------------------
// include
// -----------------------------------------
#include <iostream>
#include "util.h"
#include "ftypbox.h"
// -----------------------------------------
// define
// -----------------------------------------

// -----------------------------------------
// global value
// -----------------------------------------

// -----------------------------------------
// class/function
// -----------------------------------------
FtypBox::FtypBox()
    : m_major_brand(0), m_minor_brand(0), m_num_of_brand(0), m_compatible_brands()
{
    ;
}

FtypBox::~FtypBox()
{
    ;
}

void FtypBox::ReadBox(BitStream *p_bitstream)
{
    ReadBoxHeader(p_bitstream);
    m_major_brand = p_bitstream->Read32Bits();
    m_minor_brand = p_bitstream->Read32Bits();

    m_num_of_brand = p_bitstream->NumBytesLeft() / 4;
    UTIL_ASSERT(m_num_of_brand <= MAX_BRAND, "Invalid NumOfBrand");

    m_compatible_brands.clear();
    m_compatible_brands.reserve(m_num_of_brand);
    for (UINT8 i = 0; i < m_num_of_brand; i++)
    {
        // m_compatible_brands[i] = p_bitstream->Read32Bits();
        m_compatible_brands.push_back(p_bitstream->Read32Bits());
    }
}

void FtypBox::Print()
{
    UTIL_PRINT("ftypbox major_brand : 0x%lx\n", m_major_brand);
    UTIL_PRINT("ftypbox minor_brand : 0x%lx\n", m_minor_brand);
    for (UINT8 i = 0; i < m_compatible_brands.size(); i++)
    {
        UTIL_PRINT("ftypbox compatible_brands : 0x%lx\n", m_compatible_brands[i]);
    }
}