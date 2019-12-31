// -----------------------------------------
// include
// -----------------------------------------
#include <iostream>
#include <cstring>
#include "util.h"
#include "bitstream.h"

// -----------------------------------------
// define
// -----------------------------------------

// -----------------------------------------
// global value
// -----------------------------------------

// -----------------------------------------
// class/function
// -----------------------------------------

BitStream::BitStream(CHAR *p_buffer, UINT64 buffer_size)
    : mp_buffer(p_buffer), m_byte_buffer_size(buffer_size), m_byte_offset(0),
      m_num_bits_left(0), m_bit_buffer(0)
{
    ;
}

BitStream::~BitStream()
{
    ;
}
UINT64 BitStream::NumBytesLeft() const
{
    return m_byte_buffer_size - m_byte_offset;
}

bool BitStream::EndOfBuffer() const
{
    return NumBytesLeft() <= 0;
}

BitStream *BitStream::CreateSubBitStream(UINT64 size)
{
    BitStream *p_sub_bitstream = new BitStream(&mp_buffer[m_byte_offset], size);
    m_byte_offset += size;
    return p_sub_bitstream;
}

BitStream *BitStream::DestroySubBitStream(BitStream *p_sub_bitstream)
{
    delete p_sub_bitstream;
    return (BitStream *)nullptr;
}

UINT64 BitStream::GetPosition() const
{
    return m_byte_offset;
}

void BitStream::SetPosition(UINT64 position)
{
    m_byte_offset = position;
}

void BitStream::Write8Bits(UINT8 bits)
{
    mp_buffer[m_byte_offset++] = bits;
    // std::memcpy(&mp_buffer[m_byte_offset], &bits, 1);
}

void BitStream::Write16Bits(UINT16 bits)
{
    mp_buffer[m_byte_offset++] = static_cast<UINT8>((bits >> 8) & 0xff);
    mp_buffer[m_byte_offset++] = static_cast<UINT8>(bits & 0xff);
}

void BitStream::Write24Bits(UINT32 bits)
{
    mp_buffer[m_byte_offset++] = static_cast<UINT8>((bits >> 16) & 0xff);
    mp_buffer[m_byte_offset++] = static_cast<UINT8>((bits >> 8) & 0xff);
    mp_buffer[m_byte_offset++] = static_cast<UINT8>((bits)&0xff);
}
void BitStream::Write32Bits(UINT32 bits)
{
    mp_buffer[m_byte_offset++] = static_cast<UINT8>((bits >> 24) & 0xff);
    mp_buffer[m_byte_offset++] = static_cast<UINT8>((bits >> 16) & 0xff);
    mp_buffer[m_byte_offset++] = static_cast<UINT8>((bits >> 8) & 0xff);
    mp_buffer[m_byte_offset++] = static_cast<UINT8>((bits)&0xff);
}

void BitStream::Write64Bits(UINT64 bits)
{
    mp_buffer[m_byte_offset++] = static_cast<UINT8>((bits >> 56) & 0xff);
    mp_buffer[m_byte_offset++] = static_cast<UINT8>((bits >> 48) & 0xff);
    mp_buffer[m_byte_offset++] = static_cast<UINT8>((bits >> 40) & 0xff);
    mp_buffer[m_byte_offset++] = static_cast<UINT8>((bits >> 32) & 0xff);
    mp_buffer[m_byte_offset++] = static_cast<UINT8>((bits >> 24) & 0xff);
    mp_buffer[m_byte_offset++] = static_cast<UINT8>((bits >> 16) & 0xff);
    mp_buffer[m_byte_offset++] = static_cast<UINT8>((bits >> 8) & 0xff);
    mp_buffer[m_byte_offset++] = static_cast<UINT8>((bits)&0xff);
}

UINT8 BitStream::Read8Bits()
{
    UTIL_ASSERT(IsByteAligned(), "not byte aligned");

    const UINT8 bits = static_cast<UINT8>(mp_buffer[m_byte_offset++]);
    return bits;
}

UINT16 BitStream::Read16Bits()
{
    UTIL_ASSERT(IsByteAligned(), "not byte aligned");

    UINT16 bits = static_cast<UINT8>(mp_buffer[m_byte_offset++]);
    bits = (bits << 8) | static_cast<UINT8>(mp_buffer[m_byte_offset++]);
    return bits;
}

UINT32 BitStream::Read24Bits()
{
    UTIL_ASSERT(IsByteAligned(), "not byte aligned");

    UINT32 bits = static_cast<UINT8>(mp_buffer[m_byte_offset++]);
    bits = (bits << 8) | static_cast<UINT8>(mp_buffer[m_byte_offset++]);
    bits = (bits << 8) | static_cast<UINT8>(mp_buffer[m_byte_offset++]);
    return bits;
}

UINT32 BitStream::Read32Bits()
{
    UTIL_ASSERT(IsByteAligned(), "not byte aligned");

    UINT32 bits = static_cast<UINT8>(mp_buffer[m_byte_offset++]);
    bits = (bits << 8) | static_cast<UINT8>(mp_buffer[m_byte_offset++]);
    bits = (bits << 8) | static_cast<UINT8>(mp_buffer[m_byte_offset++]);
    bits = (bits << 8) | static_cast<UINT8>(mp_buffer[m_byte_offset++]);
    return bits;
}

UINT64 BitStream::Read64Bits()
{
    UTIL_ASSERT(IsByteAligned(), "not byte aligned");

    UINT64 bits = static_cast<UINT8>(mp_buffer[m_byte_offset++]);
    bits = (bits << 8) | static_cast<UINT8>(mp_buffer[m_byte_offset++]);
    bits = (bits << 8) | static_cast<UINT8>(mp_buffer[m_byte_offset++]);
    bits = (bits << 8) | static_cast<UINT8>(mp_buffer[m_byte_offset++]);
    bits = (bits << 8) | static_cast<UINT8>(mp_buffer[m_byte_offset++]);
    bits = (bits << 8) | static_cast<UINT8>(mp_buffer[m_byte_offset++]);
    bits = (bits << 8) | static_cast<UINT8>(mp_buffer[m_byte_offset++]);
    bits = (bits << 8) | static_cast<UINT8>(mp_buffer[m_byte_offset++]);
    return bits;
}

UINT32 BitStream::ReadBits(UINT32 len)
{
    UINT32 return_bits = 0;
    UINT32 read_bits = 0;

    if (len == 0)
    {
        return 0;
    }

    if (len > 8)
    {
        return_bits = ReadBits(8) << (len - 8);
        return_bits |= ReadBits(len - 8);
        return return_bits;
    }

    if (m_num_bits_left >= len)
    {
        return_bits = m_bit_buffer >> (8 - len);
        m_bit_buffer = (m_bit_buffer << len) & 0xFF;
        m_num_bits_left -= len;
    }
    else
    {
        read_bits = Read8Bits();

        m_bit_buffer = (m_bit_buffer << m_num_bits_left) | read_bits;
        m_num_bits_left += 8;
        return_bits = m_bit_buffer >> (m_num_bits_left - len);
        m_bit_buffer = ((m_bit_buffer << (8 - (m_num_bits_left - len))) & 0xFF);
        m_num_bits_left -= len;
    }

    return return_bits;
}

bool BitStream::IsByteAligned()
{
    return m_num_bits_left == 0;
}

void BitStream::ReadZeroTerminatedString(std::string &str)
{
    str.clear();

    while (0 < NumBytesLeft())
    {
        CHAR s = Read8Bits();

        if (s == 0)
        {
            return;
        }

        str += s;
    }
}