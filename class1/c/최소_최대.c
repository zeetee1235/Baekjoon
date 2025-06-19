#include <stdio.h>

int main(void){
    int n;
    scanf("%d", &n);
    int numbers[n];
    for (int i = 0; i < n; i++) {
        scanf("%d", &numbers[i]);
    }
    
    int max = numbers[0];
    int min = numbers[0];

    for (int i = 0; i < n; i++) {
        if (numbers[i] > max) {
            max = numbers[i];
        }
    }
    for (int i = 0; i < n; i++) {
        if (numbers[i] < min) {
            min = numbers[i];
        }
    }
    printf("%d %d\n", min, max);
    return 0;

}