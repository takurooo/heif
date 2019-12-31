#ifndef HDLRBOX_H
#define HDLRBOX_H

#include "type.h"
#include "fullbox.h"
#include "bitstream.h"
#include <string>

class HdlrBox : public FullBox
{
public:
    HdlrBox();
    ~HdlrBox();

    void ReadBox(BitStream *p_bitstream);
    void Print();

private:
    UINT32 m_handler_type;
    std::string m_name;
};

#endif