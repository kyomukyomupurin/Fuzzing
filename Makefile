CC = g++-10
CFLAGS = -std=c++20 -O1 -fsplit-stack

sol: sol.cc
	$(CC) $(CFLAGS) sol.cc -o sol

stupid: stupid.cc
	$(CC) $(CFLAGS) stupid.cc -o stupid

gen: gen.cc
	$(CC) $(CFLAGS) gen.cc -o gen

.PHONY: clean

clean:
	-rm -f sol
	-rm -f stupid
	-rm -f gen
	-rm -f sol.txt
	-rm -f stupid.txt
	-rm -f gen.txt