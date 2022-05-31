#include <exception>
#include <iostream>
#include <string>
#include <stack>
#include <stdexcept>

using namespace std;

// return a/d, round down even for negatives
// -7/3 = -3 (instead of -2 in C++)
int mydiv(int a, int d)
{
    if (d == 0) {
        throw std::runtime_error("error: divide by zero");
    }
    int ret = a/d;
    if (ret < 0 && a%d != 0)
        --ret;
    return ret;
}

#define OP_ADD 0
#define OP_SUB 1
#define OP_MUL 2
#define OP_DIV 3

stack<int> opter, oprnd;
int p1 = 0, p2 = 0;

void read_one_pair_braces(const char* data, int& i)
{
    // (div (sub 42 (mul (add 1 2) (div -7 3))) (add 5 8))
    if (data[i+1] == 'a' && data[i+2] == 'd' && data[i+3] == 'd') {
        opter.push(OP_ADD);
    }
    else if (data[i+1] == 's' && data[i+2] == 'u' && data[i+3] == 'b') {
        opter.push(OP_SUB);
    }
    else if (data[i+1] == 'm' && data[i+2] == 'u' && data[i+3] == 'l') {
        opter.push(OP_MUL);
    }
    else if (data[i+1] == 'd' && data[i+2] == 'i' && data[i+3] == 'v') {
        opter.push(OP_DIV);
    }
    i += 5;

    // read p1
    if (data[i] == '(') {
        read_one_pair_braces(data, i);
    }
    else {
        int beg = i;
        while (data[i] != ' ')
          ++i;
        string s1(data + beg, i - beg);
        p1 = stoi(s1);
        oprnd.push(p1);
        //cout << "p1 = " << p1 << '\n';
    }
    ++i; // skip the whitespace between p1 and p2

    // read p2
    if (data[i] == '(') {
        read_one_pair_braces(data, i);
    }
    else {
        int beg = i;
        while (data[i] != ')')
            ++i;
        string s2(data + beg, i - beg);
        p2 = stoi(s2);
        oprnd.push(p2);
        //cout << "p2 = " << p2 << '\n';
    }
    ++i; // skip ')'

    // perform "p1 op p2"
    int result = 0;
    int op_type = opter.top();
    opter.pop();
    p2 = oprnd.top();
    oprnd.pop();
    p1 = oprnd.top();
    oprnd.pop();
    if (op_type == OP_ADD)
        result = p1 + p2;
    else if (op_type == OP_SUB)
        result = p1 - p2;
    else if (op_type == OP_MUL)
        result = p1 * p2;
    else if (op_type == OP_DIV)
        result = mydiv(p1, p2);
    oprnd.push(result);
    //cout << "result = " << result << '\n';
}

int main()
{
    string buf;
    while (getline(cin, buf)) {
        const char* data = buf.data();
        int i = 0;
        try {
            read_one_pair_braces(data, i);
            cout << oprnd.top() << '\n';
            oprnd.pop();
        }
        catch (const std::exception& e) {
            cerr << e.what() << endl;
        }
        catch (...) {
            cerr << "some unknown error happened" << endl;
        }
    }
    return 0;
}
