#ifndef PITMBOX_H
#define PITMBOX_H

#include "type.h"
#include "fullbox.h"
#include "bitstream.h"
#include <string>

class PitmBox : public FullBox
{
public:
    PitmBox();
    ~PitmBox();

    void ReadBox(BitStream *p_bitstream);
    void Print();

private:
    UINT16 m_item_ID;
};

#endif