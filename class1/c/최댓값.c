#include <stdio.h>

int main(void) {
    int numbers[9];
    int i;
    int max;
    int index;
    
    for (i = 0; i < 9; i++) {
        scanf("%d", &numbers[i]);
    }
    
    max = numbers[0];
    index = 0;
    
    for (i = 1; i < 9; i++) {
        if (numbers[i] > max) {
            max = numbers[i];
            index = i;
        }
    }
    
    printf("%d\n%d\n", max, index + 1);
    
    return 0;
}