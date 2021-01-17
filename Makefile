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
	-rm sol
	-rm stupid
	-rm gen
	-rm sol.txt &> /dev/null
	-rm stupid.txt &> /dev/null
	-rm gen.txt