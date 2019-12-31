CC = g++
CFLAGS = -std=c++14
OBJS = main.o  util.o boxreader.o bitstream.o box.o fullbox.o ftypbox.o metabox.o mdatbox.o hdlrbox.o pitmbox.o iinfbox.o ilocbox.o
PROGRAM = a.out

all:	$(PROGRAM)

$(PROGRAM): $(OBJS)
	$(CC) $(OBJS) $(CFLAGS) -o $(PROGRAM)

.PHONY: clean
clean:
	rm -f *.o $(PROGRAM)