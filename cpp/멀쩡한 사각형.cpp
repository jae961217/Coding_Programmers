using namespace std;

long long GCD(long a, long b)
{
    if (a < b)
    {
        long tmp = a;
        a = b;
        b = tmp;
    }
    if (a % b == 0)
        return b;
    return GCD(b, a % b);
}

long long solution(int w, int h) {
    long wl = (long)w;
    long hl = (long)h;
    long long answer = 1;
    answer = wl * hl;
    answer = answer - wl - hl + GCD(wl, hl);

    return answer;
}