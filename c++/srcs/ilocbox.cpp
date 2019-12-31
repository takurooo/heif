// -----------------------------------------
// include
// -----------------------------------------
#include <iostream>
#include "util.h"
#include "ilocbox.h"
// -----------------------------------------
// define
// -----------------------------------------

// -----------------------------------------
// global value
// -----------------------------------------

// -----------------------------------------
// class/function
// -----------------------------------------
IlocBox::IlocBox()
    : m_offset_size(0), m_length_size(0),
      m_base_offset_size(0), m_index_size(0), m_item_count(0),
      m_iloc_list()
{
    ;
}

IlocBox::~IlocBox()
{
    ;
}

void IlocBox::ReadBox(BitStream *p_bitstream)
{
    ReadFullBoxHeader(p_bitstream);
    m_offset_size = static_cast<UINT8>(p_bitstream->ReadBits(4));
    m_length_size = static_cast<UINT8>(p_bitstream->ReadBits(4));
    m_base_offset_size = static_cast<UINT8>(p_bitstream->ReadBits(4));

    if (GetVersion() == 1 || GetVersion() == 2)
    {
        m_index_size = static_cast<UINT8>(p_bitstream->ReadBits(4));
    }
    else
    {
        p_bitstream->ReadBits(4);
    }

    if (GetVersion() < 2)
    {
        m_item_count = static_cast<UINT32>(p_bitstream->Read16Bits());
    }
    else if (GetVersion() == 2)
    {
        m_item_count = p_bitstream->Read32Bits();
    }

    for (UINT8 i = 0; i < m_item_count; i++)
    {
        IlocElement iloc_elm = {0};

        if (GetVersion() < 2)
        {
            iloc_elm.item_ID = p_bitstream->Read16Bits();
        }
        else if (GetVersion() == 2)
        {
            iloc_elm.item_ID = p_bitstream->Read32Bits();
        }

        if (GetVersion() == 1 || GetVersion() == 2)
        {
            p_bitstream->ReadBits(12);
            iloc_elm.construction_method = static_cast<ConstructionMethod>(p_bitstream->ReadBits(4));
        }

        iloc_elm.data_reference_index = p_bitstream->Read16Bits();
        iloc_elm.base_offset = p_bitstream->ReadBits(m_base_offset_size * 8);

        const UINT16 extent_count = p_bitstream->Read16Bits();

        for (UINT8 j = 0; j < extent_count; j++)
        {
            IlocExtentElement iloc_extent_elm = {0};
            if ((GetVersion() == 1 || GetVersion() == 2) && m_index_size > 0)
            {
                iloc_extent_elm.extent_index = p_bitstream->ReadBits(m_index_size * 8);
            }
            iloc_extent_elm.extent_offset = p_bitstream->ReadBits(m_offset_size * 8);
            iloc_extent_elm.extent_length = p_bitstream->ReadBits(m_length_size * 8);

            iloc_elm.iloc_extent_list.push_back(iloc_extent_elm);
        }
        m_iloc_list.push_back(iloc_elm);
    }
}

void IlocBox::Print()
{

    UTIL_PRINT("ilocbox offset_size : %d\n", m_offset_size);
    UTIL_PRINT("ilocbox length_size : %d\n", m_length_size);
    UTIL_PRINT("ilocbox base_offset_size : %d\n", m_base_offset_size);
    UTIL_PRINT("ilocbox index_size : %d\n", m_index_size);
    UTIL_PRINT("ilocbox item_count : %ld\n", m_item_count);

    for (UINT8 i = 0; i < m_iloc_list.size(); i++)
    {
        IlocElement &iloc_elm = m_iloc_list[i];
        UTIL_PRINT("ilocbox elm[%d] item_ID : 0x%lx\n", i, iloc_elm.item_ID);
        UTIL_PRINT("ilocbox elm[%d] construction_method : 0x%x\n", i, iloc_elm.construction_method);
        UTIL_PRINT("ilocbox elm[%d] data_reference_index : 0x%x\n", i, iloc_elm.data_reference_index);
        UTIL_PRINT("ilocbox elm[%d] base_offset : 0x%llx\n", i, iloc_elm.base_offset);

        for (UINT8 j = 0; j < m_iloc_list[i].iloc_extent_list.size(); j++)
        {
            IlocExtentElement &iloc_ext_elm = m_iloc_list[i].iloc_extent_list[j];
            UTIL_PRINT("ilocbox elm[%d] extelm[%d] extent_index : 0x%llx\n", i, j, iloc_ext_elm.extent_index);
            UTIL_PRINT("ilocbox elm[%d] extelm[%d] extent_offset : 0x%llx\n", i, j, iloc_ext_elm.extent_offset);
            UTIL_PRINT("ilocbox elm[%d] extelm[%d] extent_length : 0x%llx\n", i, j, iloc_ext_elm.extent_length);
        }
    }
}