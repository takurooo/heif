// -----------------------------------------
// include
// -----------------------------------------
#include <iostream>
#include "fullbox.h"
// -----------------------------------------
// define
// -----------------------------------------

// -----------------------------------------
// global value
// -----------------------------------------

// -----------------------------------------
// class/function
// -----------------------------------------

FullBox::FullBox()
    : m_version(0), m_flags(0)
{
    ;
}

FullBox::~FullBox()
{
    ;
}

UINT8 FullBox::GetVersion() const
{
    return m_version;
}

void FullBox::ReadFullBoxHeader(BitStream *p_bitstream)
{
    ReadBoxHeader(p_bitstream);

    m_version = p_bitstream->Read8Bits();
    m_flags = p_bitstream->Read24Bits();
}