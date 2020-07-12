
SRCDIR := .
SRCS := $(wildcard $(SRCDIR)/*.cpp)
# SRC := main.cpp  util.cpp boxreader.cpp bitstream.cpp \
# 		box.cpp fullbox.cpp ftypbox.cpp metabox.cpp \
# 		mdatbox.cpp hdlrbox.cpp pitmbox.cpp iinfbox.cpp ilocbox.cpp
OBJS := $(SRCS:.cpp=.o)
INCDIR := $(SRCDIR)
CC := g++
CFLAGS := -std=c++14
PROGRAM := a.out

# for debug
# $(warning CFLAGS = $(CFLAGS))
# $(warning OBJS = $(OBJS))
# $(warning SRCS = $(SRCS))

all:	$(PROGRAM)

$(PROGRAM): $(OBJS)
	$(CC) $(CFLAGS) $(OBJS) -o $(PROGRAM)

.PHONY: clean # task target
clean:
	rm -f $(OBJS) $(PROGRAM)
