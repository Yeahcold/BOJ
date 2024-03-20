#include <bits/stdc++.h>
using namespace std;

int main(){
    ios::sync_with_stdio(0);
    cin.tie(0);
    int N, a[10] = {}, num = 0;
    cin >> N;

    while (N) {
        if (N%10 == 9 ) a[6] += 1;
        else a[N%10] += 1;
        N /= 10;
    }
    a[6] = (a[6]+1)/2;
    for (int i : a)
        if (num < i) num = i;
    cout << num;
}