// -----------------------------------------
// include
// -----------------------------------------
#include <iostream>
#include "util.h"
#include "fourcc.h"
#include "iinfbox.h"
// -----------------------------------------
// define
// -----------------------------------------

// -----------------------------------------
// global value
// -----------------------------------------

// -----------------------------------------
// class/function
// -----------------------------------------
ItemInfoEntry::ItemInfoEntry()
    : m_item_ID(0), m_item_protection_index(0),
      m_item_name(""), m_content_type(""),
      m_content_encoding(""), m_extension_type(0),
      m_item_type(0), m_item_uri_type("")
{
}

ItemInfoEntry::~ItemInfoEntry()
{
    ;
}

UINT32 ItemInfoEntry::GetItemID() const
{
    return m_item_ID;
}

void ItemInfoEntry::ReadBox(BitStream *p_bitstream)
{
    ReadFullBoxHeader(p_bitstream);
    if (GetVersion() == 0 || GetVersion() == 1)
    {
        m_item_ID = p_bitstream->Read16Bits();
        m_item_protection_index = p_bitstream->Read16Bits();
        p_bitstream->ReadZeroTerminatedString(m_item_name);
        p_bitstream->ReadZeroTerminatedString(m_content_type);
        if (p_bitstream->NumBytesLeft() > 0)
        {
            p_bitstream->ReadZeroTerminatedString(m_content_encoding);
        }
    }

    if (GetVersion() == 1)
    {
        if (p_bitstream->NumBytesLeft() > 0)
        {
            m_extension_type = p_bitstream->Read32Bits();
        }
        if (p_bitstream->NumBytesLeft() > 0)
        {
            // ItemInfoExtension(extension_type); //optional
            // TODO
        }
    }

    if (GetVersion() >= 2)
    {
        if (GetVersion() == 2)
        {
            m_item_ID = p_bitstream->Read16Bits();
        }
        else if (GetVersion() == 3)
        {
            m_item_ID = p_bitstream->Read32Bits();
        }
        m_item_protection_index = p_bitstream->Read16Bits();
        m_item_type = p_bitstream->Read32Bits();
        p_bitstream->ReadZeroTerminatedString(m_item_name);

        if (m_item_type == FOURCC::MIME)
        {
            p_bitstream->ReadZeroTerminatedString(m_content_type);
            if (p_bitstream->NumBytesLeft() > 0)
            {
                p_bitstream->ReadZeroTerminatedString(m_content_encoding);
            }
        }
        else if (m_item_type == FOURCC::URI)
        {
            p_bitstream->ReadZeroTerminatedString(m_item_uri_type);
        }
    }
}

void ItemInfoEntry::Print()
{
    UTIL_PRINT("iteminfo m_item_ID : 0x%x\n", m_item_ID);
    UTIL_PRINT("iteminfo m_item_protection_index : 0x%hx\n", m_item_protection_index);
    UTIL_PRINT("iteminfo m_item_name : %s\n", m_item_name.c_str());
    UTIL_PRINT("iteminfo m_content_type : %s\n", m_content_type.c_str());
    UTIL_PRINT("iteminfo m_content_encoding : %s\n", m_content_encoding.c_str());
    UTIL_PRINT("iteminfo m_extension_type : %ld\n", m_extension_type);
    UTIL_PRINT("iteminfo m_item_type : 0x%lx\n", m_item_type);
    UTIL_PRINT("iteminfo m_item_uri_type : %s\n", m_item_uri_type.c_str());
}

IinfBox::IinfBox()
    : m_entry_count(0), m_item_infos(), m_item_IDs()
{
    ;
}

IinfBox::~IinfBox()
{
    ;
}

void IinfBox::ReadBox(BitStream *p_bitstream)
{
    ReadFullBoxHeader(p_bitstream);
    if (GetVersion() == 0)
    {
        m_entry_count = (UINT32)p_bitstream->Read16Bits();
    }
    else
    {
        m_entry_count = (UINT32)p_bitstream->Read32Bits();
    }

    m_item_infos.reserve(m_entry_count);
    m_item_IDs.reserve(m_entry_count);

    for (UINT8 i = 0; i < m_entry_count; i++)
    {
        // read box type adn size
        UINT32 box_size = p_bitstream->Read32Bits();
        UINT32 box_type = p_bitstream->Read32Bits();
        p_bitstream->SetPosition(p_bitstream->GetPosition() - 8);
        UTIL_PRINT("Pos 0x%0llx BoxSize 0x%lx BoxType 0x%lx\n", p_bitstream->GetPosition(), box_size, box_type);

        BitStream *p_sub_bitstream = p_bitstream->CreateSubBitStream((UINT64)box_size);
        UTIL_ASSERT(p_sub_bitstream != nullptr, "p_sub_bitstrema is NULL.");

        ItemInfoEntry infoEntry;

        infoEntry.ReadBox(p_sub_bitstream);

        m_item_IDs.push_back(infoEntry.GetItemID());

        m_item_infos.push_back(infoEntry);

        p_sub_bitstream = p_bitstream->DestroySubBitStream(p_sub_bitstream);
    }
}

void IinfBox::Print()
{
    UTIL_PRINT("iinfbox m_entry_count : %lu\n", m_entry_count);
    for (UINT8 i = 0; i < m_entry_count; i++)
    {
        m_item_infos[i].Print();
    }
}