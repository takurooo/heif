// -----------------------------------------
// include
// -----------------------------------------
#include <iostream>
#include "util.h"
#include "fourcc.h"
#include "metabox.h"
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

MetaBox::MetaBox()
    : m_hdlr(), m_pitm(), m_iinf(), m_iloc()
{
    ;
}

MetaBox::~MetaBox()
{
    ;
}

void MetaBox::ReadBox(BitStream *p_bitstream)
{
    ReadFullBoxHeader(p_bitstream);
    while (p_bitstream->NumBytesLeft() >= 8)
    {
        // read box type adn size
        UINT32 box_size = p_bitstream->Read32Bits();
        UINT32 box_type = p_bitstream->Read32Bits();
        p_bitstream->SetPosition(p_bitstream->GetPosition() - 8);
        UTIL_PRINT("Pos 0x%0llx BoxSize 0x%lx BoxType 0x%lx\n", p_bitstream->GetPosition(), box_size, box_type);

        BitStream *p_sub_bitstream = p_bitstream->CreateSubBitStream((UINT64)box_size);
        UTIL_ASSERT(p_sub_bitstream != nullptr, "p_sub_bitstrema is NULL.");

        switch (box_type)
        {
        case FOURCC::HDLR:
            UTIL_PRINT("found hdlr\n");
            m_hdlr.ReadBox(p_sub_bitstream);
            m_hdlr.Print();
            break;
        case FOURCC::DINF:
            UTIL_PRINT("found dinf\n");
            break;
        case FOURCC::PITM:
            UTIL_PRINT("found pitm\n");
            m_pitm.ReadBox(p_sub_bitstream);
            m_pitm.Print();
            break;
        case FOURCC::ILOC:
            UTIL_PRINT("found iloc\n");
            m_iloc.ReadBox(p_sub_bitstream);
            m_iloc.Print();
            break;
        case FOURCC::IINF:
            UTIL_PRINT("found iinf\n");
            m_iinf.ReadBox(p_sub_bitstream);
            m_iinf.Print();
            break;
        case FOURCC::IREF:
            UTIL_PRINT("found iref\n");
            break;
        case FOURCC::IPRP:
            UTIL_PRINT("found iprp\n");
            break;
        default:
            UTIL_ERR_PRINT("invalid box_type %lx\n", box_type);
            UTIL_ASSERT(0, "");
            break;
        }

        p_sub_bitstream = p_bitstream->DestroySubBitStream(p_sub_bitstream);
        // break; // TODO debug
    }
    UTIL_PRINT("ReadBoxes End\n");
}

void MetaBox::Print()
{
    ;
}