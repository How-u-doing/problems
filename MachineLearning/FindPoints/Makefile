CXX := g++
CXXFLAGS := -std=c++17 -Wall -Wextra

.PHONY: clean

find_points: find_points.cc
	$(CXX) $(CXXFLAGS) -g -o $@ $<

clean:
	rm -f find_points
