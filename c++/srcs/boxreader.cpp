// -----------------------------------------
// include
// -----------------------------------------
#include <iostream>
#include <cstring>
#include "boxreader.h"
#include "fourcc.h"
#include "util.h"

// -----------------------------------------
// define
// -----------------------------------------

// -----------------------------------------
// global value
// -----------------------------------------

// -----------------------------------------
// class/function
// -----------------------------------------

BoxReader::BoxReader(CHAR *p_buffer, UINT64 file_size)
    : m_bitstream(p_buffer, file_size), m_ftyp(), m_meta(), m_mdat()
{
    ;
}

BoxReader::~BoxReader()
{
    ;
}

void BoxReader::ReadBox()
{
}

void BoxReader::ReadBoxes()
{
    UTIL_PRINT("ReadBoxes Start\n");

    while (m_bitstream.NumBytesLeft() >= 8)
    {
        UINT32 box_type, box_size;
        ReadHeader(box_type, box_size);

        BitStream *p_sub_bitstream = m_bitstream.CreateSubBitStream((UINT64)box_size);
        UTIL_ASSERT(p_sub_bitstream != nullptr, "p_sub_bitstrema is NULL.");

        switch (box_type)
        {
        case FOURCC::FTYP:
            UTIL_PRINT("found ftyp\n");
            m_ftyp.ReadBox(p_sub_bitstream);
            // m_ftyp.Print();
            break;
        case FOURCC::META:
            UTIL_PRINT("found meta\n");
            m_meta.ReadBox(p_sub_bitstream);
            break;
        case FOURCC::MDAT:
            UTIL_PRINT("found mdat\n");
            m_mdat.ReadBox(p_sub_bitstream);
            break;
        default:
            UTIL_ERR_PRINT("invalid box_type %lx\n", box_type);
            UTIL_ASSERT(0, "");
            break;
        }

        p_sub_bitstream = m_bitstream.DestroySubBitStream(p_sub_bitstream);
        // break; // TODO debug
    }
    UTIL_PRINT("ReadBoxes End\n");
}

void BoxReader::ReadHeader(UINT32 &box_type, UINT32 &box_size)
{
    box_size = m_bitstream.Read32Bits();
    box_type = m_bitstream.Read32Bits();
    UINT64 cur_position = m_bitstream.GetPosition();
    m_bitstream.SetPosition(cur_position - 8);
    UTIL_PRINT("Pos 0x%0llx BoxSize 0x%lx BoxType 0x%lx\n", m_bitstream.GetPosition(), box_size, box_type);
}