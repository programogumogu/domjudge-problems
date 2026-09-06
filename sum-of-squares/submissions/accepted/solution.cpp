#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    long long N;
    cin >> N;

    long long ans = 0;
    for (long long i = 0; i < N; i++) {
        long long x;
        cin >> x;
        ans += x * x;
    }

    cout << ans << "\n";
    return 0;
}
