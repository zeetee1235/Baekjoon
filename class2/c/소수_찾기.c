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
        if (num < 2) continue;
        int prime = 1;
        for (int j = 2; j * j <= num; j++) {
            if (num % j == 0) {
                prime = 0;
                break;
            }
        }
        if (prime) sum++;
    }
    printf("%d\n", sum);
    return 0;
}
