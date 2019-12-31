// -----------------------------------------
// include
// -----------------------------------------
#include <iostream>
#include "util.h"
#include "hdlrbox.h"
// -----------------------------------------
// define
// -----------------------------------------

// -----------------------------------------
// global value
// -----------------------------------------

// -----------------------------------------
// class/function
// -----------------------------------------
HdlrBox::HdlrBox()
    : m_handler_type(0), m_name("")
{
    ;
}

HdlrBox::~HdlrBox()
{
    ;
}

void HdlrBox::ReadBox(BitStream *p_bitstream)
{
    ReadFullBoxHeader(p_bitstream);
    p_bitstream->Read32Bits();
    m_handler_type = p_bitstream->Read32Bits();
    p_bitstream->Read32Bits();
    p_bitstream->Read32Bits();
    p_bitstream->Read32Bits();
    p_bitstream->ReadZeroTerminatedString(m_name);
}

void HdlrBox::Print()
{
    UTIL_PRINT("hdlrbox m_handler_type : 0x%lx\n", m_handler_type);
    UTIL_PRINT("hdlrbox m_name : %s\n", m_name.c_str());
}