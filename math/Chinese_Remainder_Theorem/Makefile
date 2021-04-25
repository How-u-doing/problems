CXX := g++
CXXFLAGS := -std=c++17 -Wall -g

crt := Chinese_Remainder_Theorem

.PHONY: all clean

all: $(crt) 

$(crt): % : %.cpp
	$(CXX) $(CXXFLAGS) -o $@ $<

clean:
	rm -f $(crt)
