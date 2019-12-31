#ifndef IINFBOX_H
#define IINFBOX_H

#include <string>
#include <vector>
#include "type.h"
#include "fullbox.h"
#include "bitstream.h"

class ItemInfoEntry : public FullBox
{
public:
    ItemInfoEntry();
    ~ItemInfoEntry();

    UINT32 GetItemID() const;
    void ReadBox(BitStream *p_bitstream);
    void Print();

private:
    UINT16 m_item_ID;
    UINT16 m_item_protection_index;
    std::string m_item_name;
    std::string m_content_type;
    std::string m_content_encoding;

    UINT32 m_extension_type;

    UINT32 m_item_type;
    std::string m_item_uri_type;
};

class IinfBox : public FullBox
{
public:
    IinfBox();
    ~IinfBox();

    void ReadBox(BitStream *p_bitstream);
    void Print();

private:
    UINT32 m_entry_count;
    std::vector<ItemInfoEntry> m_item_infos;
    std::vector<UINT32> m_item_IDs;
};

#endif