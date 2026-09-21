#include <iostream>
#include <string>

using namespace std;
int solution(int n)
{
    string strn = to_string(n);
    int answer = 0;
    int i;
    for (i=0; i < strn.length(); i++){
            answer += (int(strn[i]) - 48);
    }
    
    return answer;
}