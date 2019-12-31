// -----------------------------------------
// include
// -----------------------------------------
#include <iostream>
#include "util.h"
#include "pitmbox.h"
// -----------------------------------------
// define
// -----------------------------------------

// -----------------------------------------
// global value
// -----------------------------------------

// -----------------------------------------
// class/function
// -----------------------------------------
PitmBox::PitmBox()
    : m_item_ID(0)
{
    ;
}

PitmBox::~PitmBox()
{
    ;
}

void PitmBox::ReadBox(BitStream *p_bitstream)
{
    ReadFullBoxHeader(p_bitstream);
    m_item_ID = p_bitstream->Read16Bits();
}

void PitmBox::Print()
{
    UTIL_PRINT("pitmbox m_item_ID : 0x%x\n", m_item_ID);
}