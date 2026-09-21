#include <string>
#include <vector>

using namespace std;

int SumDigit(int n) {
    int result = 0;
    for (int i = 0; i < int(to_string(n).length()); i++) {
        result += (int(to_string(n)[i]) - '0');
    }
    return result;
}

bool solution(int x) {
    return (x%SumDigit(x) == 0) ? true : false;
}