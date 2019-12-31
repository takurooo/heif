#ifndef ILOCBOX_H
#define ILOCBOX_H

#include "type.h"
#include "fullbox.h"
#include "bitstream.h"
#include <string>

struct IlocExtentElement
{
    UINT64 extent_index;
    UINT64 extent_offset;
    UINT64 extent_length;
};

enum ConstructionMethod
{
    FILE_OFFSET = 0,
    IDAT_OFFSET = 1,
    ITEM_OFFSET = 2
};

struct IlocElement
{
    UINT32 item_ID;
    ConstructionMethod construction_method;
    UINT16 data_reference_index;
    UINT64 base_offset;
    std::vector<IlocExtentElement> iloc_extent_list;
};

class IlocBox : public FullBox
{
public:
    IlocBox();
    ~IlocBox();

    void ReadBox(BitStream *p_bitstream);
    void Print();

private:
    UINT8 m_offset_size;
    UINT8 m_length_size;
    UINT8 m_base_offset_size;
    UINT8 m_index_size;
    UINT32 m_item_count;
    std::vector<IlocElement> m_iloc_list;
};

#endif