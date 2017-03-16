
CXXFLAGS = -g -fPIC -I/usr/include/python2.7 -I../MPOST_Linux/
LDFLAGS =
LIBS = $(libMPOST)

libMPOST = ../MPOST_Linux/Release/libMPOST_Linux.a

# All Target
all: mpostmodule.so

$(libMPOST): ../MPOST_Linux/*.h ../MPOST_Linux/*.cpp
	make -C ../MPOST_Linux/Release clean all

# Tool invocations
libpympost.so: main.o $(LIBS)
	@echo 'Building target: $@'
	@echo 'Invoking: GCC C++ Linker'
	$(CXX) -rdynamic -shared -fPIC -o $@ main.o $(LIBS)
	@echo 'Finished building target: $@'
	@echo ' '

libpympost.a: main.o
	@echo 'Building target: $@'
	@echo 'Invoking: GCC C++ Linker'
	ar -r "libpympost.a" main.o
	@echo 'Finished building target: $@'
	@echo ' '

mpostmodule.so: CAcceptor.o
	$(CXX) -rdynamic -shared -fPIC -o $@ CAcceptor.o $(LIBS) -lboost_python

test: test.o main.o
	g++ -o test test.o main.o $(LIBS) -lpthread 

testso: test.o libpympost.so
	g++ -o testso test.o -lpthread -L. -lpympost

# Other Targets
clean:
	-$(RM) *.o *.so *.a main.o libpympost.so libpympost.a test testso test.o
	-@echo ' '

TAGS:
	etags *.cpp ../MPOST_Linux/*.h ../MPOST_Linux/*.cpp

.PHONY: all clean
