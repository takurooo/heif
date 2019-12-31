#ifndef FULLBOX_H
#define FULLBOX_H

#include "type.h"
#include "box.h"
#include "bitstream.h"

class FullBox : public Box
{
public:
    FullBox();
    virtual ~FullBox();

    UINT8 GetVersion() const;

protected:
    void ReadFullBoxHeader(BitStream *p_bitstream);

private:
    UINT8 m_version;
    UINT32 m_flags;
};

#endif