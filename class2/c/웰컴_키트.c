#include <stdio.h>

int main(int argc, char const *argv[])
{
    int n;
    scanf("%d", &n);
    int size[6];
    scanf("%d %d %d %d %d %d", &size[0], &size[1], &size[2], &size[3], &size[4], &size[5]);
    int t,p;
    scanf("%d %d", &t, &p);
    int min = 0, max = 0; // min을 0으로 초기화
    
    for (int i = 0; i < 6; i++) { // 6개 모두 반복
        if (size[i] % t == 0) {
            min += size[i] / t;
        } 
        else {
            min += size[i] / t + 1;
        }
    }

    printf("%d \n", min);
    max = n / p;
    int remain = n % p;
    printf("%d %d", max, remain);

    return 0;
}
