#include <stdio.h>

int main(int argc, char const *argv[])
{
    int n;
    scanf("%d", &n);
    int ary[n];
    int sum = 0;

    for (int i = 0; i < n; i++) {
        scanf("%d", &ary[i]);
    }

    for (int i = 0; i < n; i++) {
        int num = ary[i];
        if (num < 2) continue; // 0, 1은 소수 아님
        int is_prime = 1;
        for (int j = 2; j * j <= num; j++) {
            if (num % j == 0) {
                is_prime = 0;
                break;
            }
        }
        if (is_prime) sum++;
    }
    printf("%d\n", sum);
    return 0;
}
