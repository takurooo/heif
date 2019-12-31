#ifndef METABOX_H
#define METABOX_H

#include "type.h"
#include "fullbox.h"
#include "bitstream.h"
#include "hdlrbox.h"
#include "pitmbox.h"
#include "iinfbox.h"
#include "ilocbox.h"

class MetaBox : public FullBox
{
public:
    MetaBox();
    ~MetaBox();
    void ReadBox(BitStream *p_bitstream);
    void Print();

protected:
private:
    HdlrBox m_hdlr;
    PitmBox m_pitm;
    IinfBox m_iinf;
    IlocBox m_iloc;
};

#endif