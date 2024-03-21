#include <bits/stdc++.h>
using namespace std;
int n, x, res;
int a[1000001] = {};
// 존재하는지의 여부 확인
bool b[2000001];

int main(){
    ios::sync_with_stdio(0);
    cin.tie(0);
    res = 0;
    cin >> n;
    for (int i = 0; i < n; i++) cin >> a[i];
    cin >> x;

    for (int i = 0; i < n; i++) {
        if (x-a[i] > 0 && b[x-a[i]]) res++;
        b[a[i]] = true;
    }
    cout << res;
}