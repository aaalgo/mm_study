CC = g++
CXXFLAGS += -O3 -g -std=c++11 -I/usr/include/python3.6 -Iaffy/sdk/ -D_INCLUDE_UNISTD_HEADER_=1 -fopenmp
LDFLAGS += -L/usr/lib/python3.6/config-3.6m-x86_64-linux-gnu -fopenmp
LDLIBS += -lboost_program_options -lboost_numpy3 -lboost_python3 -lpython3.6

AFFY_SRCS = affy/sdk/file/FileIO.cpp \
	    affy/sdk/file/CELFileData.cpp \
	    affy/sdk/file/CDFFileData.cpp 

AFFY_OBJS = $(AFFY_SRCS:.cpp=.o)


all:	import compare # extract_ranks


#cdfcel:	cdfcel.o $(AFFY_OBJS)
#	$(CC) -o $@ $(LDFLAGS) $^ $(LDLIBS)

#popgene:	popgene.o $(AFFY_OBJS)
#	$(CC) -o $@ $(LDFLAGS) $^ $(LDLIBS)

