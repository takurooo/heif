#include <iostream>
#include <unistd.h>
#include <fcntl.h>
#include <sys/mman.h>
#include <sys/stat.h>
#include "type.h"
#include "util.h"
#include "fourcc.h"
#include "bitstream.h"
#include "boxreader.h"
// ctrl+option+nで実行

UINT64 GetFileSize(const CHAR *file_path)
{
    struct stat statBuf;

    if (stat(file_path, &statBuf) == 0)
        return statBuf.st_size;

    return -1L;
}

UINT64 GetFileSizeForMap(const CHAR *file_path)
{
    UINT64 page_size, map_size, file_size;
    file_size = GetFileSize(file_path);
    page_size = getpagesize();
    map_size = (file_size / page_size + 1) * page_size;
    return map_size;
}

int main()
{
    UINT64 page_size, map_size, file_size;
    INT fd;
    CHAR *map;
    CHAR file_path[] = "in/test.heic";

    fd = open(file_path, O_RDWR, 0666);
    file_size = GetFileSize(file_path);
    map_size = GetFileSizeForMap(file_path);

    map = (CHAR *)mmap(NULL, map_size, PROT_READ | PROT_WRITE, MAP_SHARED, fd, 0);
    if (map == MAP_FAILED)
    {
        printf("Error : mmap failed\n");
        return -1;
    }

    BoxReader box_reader((CHAR *)map, file_size);
    box_reader.ReadBoxes();

    munmap(map, map_size);
    close(fd);
    printf("end main\n");

    return 0;
}