#ifndef MDATBOX_H
#define MDATBOX_H

#include "type.h"
#include "box.h"
#include "bitstream.h"

class MdatBox : public Box
{
public:
    MdatBox();
    ~MdatBox();
    void ReadBox(BitStream *p_bitstream);
    void Print();

protected:
private:
};

#endif