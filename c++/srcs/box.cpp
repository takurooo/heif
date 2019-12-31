// -----------------------------------------
// include
// -----------------------------------------
#include <iostream>
#include "util.h"
#include "fourcc.h"
#include "box.h"
// -----------------------------------------
// define
// -----------------------------------------

// -----------------------------------------
// global value
// -----------------------------------------

// -----------------------------------------
// class/function
// -----------------------------------------

Box::Box()
    : m_size(0), m_type(0), m_largesize(0), m_usertype(), m_strat_offset(0)
{
    ;
}

Box::~Box()
{
    ;
}

UINT32 Box::GetBoxSize() const
{
    return m_size;
}

UINT32 Box::GetBoxType() const
{
    return m_type;
}

void Box::ReadBoxHeader(BitStream *p_bitstream)
{
    m_size = p_bitstream->Read32Bits();
    m_type = p_bitstream->Read32Bits();

    if (m_size == 1)
    {
        m_largesize = p_bitstream->Read64Bits();
    }

    if (m_type == FOURCC::UUID)
    {
        for (UINT8 i = 0; i < 16; i++)
        {
            // m_usertype[i] = p_bitstream->Read8Bits();
            m_usertype.push_back(p_bitstream->Read8Bits());
        }
    }
}