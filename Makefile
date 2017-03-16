
CXXFLAGS = -g -fPIC -I/usr/include/python2.7 -I../MPOST_Linux/
LDFLAGS =
LIBS = $(libMPOST)

libMPOST = ../MPOST_Linux/Release/libMPOST_Linux.a

# All Target
all: mpostmodule.so

$(libMPOST): ../MPOST_Linux/*.h ../MPOST_Linux/*.cpp
	make -C ../MPOST_Linux/Release clean all

# Tool invocations
mpostmodule.so: CAcceptor.o
	$(CXX) -rdynamic -shared -fPIC -o $@ CAcceptor.o $(LIBS) -lboost_python

# Other Targets
clean:
	-$(RM) *.o *.so *.a
	-@echo ' '

TAGS:
	etags *.cpp ../MPOST_Linux/*.h ../MPOST_Linux/*.cpp

.PHONY: all clean
