#ifndef BITSTREAM_H
#define BITSTREAM_H

#include <string>
#include "type.h"

class BitStream
{
public:
    BitStream(CHAR *p_buffer, UINT64 buffer_size);
    ~BitStream();

    UINT64 NumBytesLeft() const;

    bool EndOfBuffer() const;

    BitStream *CreateSubBitStream(UINT64 size);

    BitStream *DestroySubBitStream(BitStream *p_sub_bitstream);

    UINT64 GetPosition() const;

    void SetPosition(UINT64 position);

    void Write8Bits(UINT8 bits);

    void Write16Bits(UINT16 bits);

    void Write24Bits(UINT32 bits);

    void Write32Bits(UINT32 bits);

    void Write64Bits(UINT64 bits);

    UINT8 Read8Bits();

    UINT16 Read16Bits();

    UINT32 Read24Bits();

    UINT32 Read32Bits();

    UINT64 Read64Bits();

    UINT32 ReadBits(UINT32 len);

    bool IsByteAligned();

    void ReadZeroTerminatedString(std::string &str);

private:
    CHAR *mp_buffer;
    UINT64 m_byte_buffer_size;
    UINT64 m_byte_offset;

    UINT32 m_num_bits_left;
    UINT32 m_bit_buffer;
};

#endif