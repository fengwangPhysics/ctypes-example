all: ../TestModule/lib/libtest.so

../TestModule/lib/libtest.so: libtest.c
	mkdir -p ../TestModule/lib
	$(CC) -Wall -g -fPIC -shared -o $@ $?

clean:
	rm -f ../TestModule/lib/libtest.so
