#include <iostream>
#include <string>
using namespace std;

int sum(int x,int y) {return (x+y);}
string sum(string x,string y) {return (x+y);}

int main()
{
    cout << sum(10,12)<<endl; // 22
    cout << sum("10","12")<<endl; // 1012
    return 0;
}


