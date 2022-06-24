CXX := g++
CXXFLAGS := -std=c++17 -Wall -Wextra

.PHONY: clean

mandelbrot: mandelbrot.cc
	$(CXX) $(CXXFLAGS) -O3 -o $@ $^

clean:
	rm -f mandelbrot
