#ifndef BOX_H
#define BOX_H

#include <vector>
#include "type.h"
#include "bitstream.h"

class Box
{
public:
    Box();
    virtual ~Box();

protected:
    void ReadBoxHeader(BitStream *p_bitstream);
    UINT32 GetBoxSize() const;
    UINT32 GetBoxType() const;

private:
    UINT32 m_size;
    UINT32 m_type;
    UINT64 m_largesize;
    // UINT8 m_usertype[16];
    std::vector<UINT8> m_usertype;
    UINT64 m_strat_offset;
};

#endif