CXX := g++
CXXFLAGS := -std=c++17 -Wall -Wextra

.PHONY: clean

calc := simple_lisp_calc

simple_lisp_calc: simple_lisp_calc.cc
	$(CXX) $(CXXFLAGS) -g -o $@ $^

clean:
	rm -f $(calc)
