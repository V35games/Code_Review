#include <iostream>
#include <string>
#include <sstream>
using namespace std;


int print_line() {
    string str;
    int inp;
    getline(cin, str);
    stringstream(str) >> inp;
    if (sizeof(inp) != sizeof(int)) {
        return -1;
    }
    for (int i = 0; i < inp; i++) {
        cout << i << endl;
    }
    return 0;
}


int main()
{
    if (print_line() == -1) {
        cerr << "input error";
        return EXIT_FAILURE;
    }   
    return 0;
}
