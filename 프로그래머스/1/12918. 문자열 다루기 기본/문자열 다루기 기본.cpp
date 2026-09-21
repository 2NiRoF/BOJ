#include <string>
#include <iostream>

using namespace std;

bool isalpha(char c) {
    if (('A' <= c && c <= 'Z') || ('a' <= c  && c <= 'z')){
        return true;
    } else return false;
}

bool solution(string s) {
    if (s.length() == 4 || s.length() == 6){
        for (int i = 0; i < s.length(); i++) {
            if (isalpha(s[i])) return false;
        } return true;
    } else return false;
}