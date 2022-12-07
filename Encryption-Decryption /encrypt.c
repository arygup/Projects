#include <stdio.h>
#include <stdlib.h>
#include <time.h>
int main(int a, char *aa[a])
{
    srand(time(0));
    int A[1000128];
    FILE *file, *ans, *key;
    file = fopen(aa[1], "r");
    ans = fopen(aa[3], "w");
    key = fopen(aa[2], "w");
    for (int i = 0; i < 127; i++)
    {
        int y;
        y = rand();
        A[i] = y % 2;
        fprintf(key, "%d", A[i]);
    }
    fclose(key);
    for (int i = 127; i < 1000128; i++)
    {
        A[i] = A[i - 1] ^ A[i - 127];
    }
    int index = 127, y, x, B[8];
    while (fscanf(file, "%c", &x) != EOF)
    {
        for (int i = 0; i < 8; i++)
        {
            int tempf = x & (1<<i);
            B[7 - i] = 0;
            if(tempf) B[7 - i] = 1;
        }
        for (int i = 0; i < 8; i++)
        {
            y = A[index] ^ B[i];
            fprintf(ans, "%d", y);
            index++;
        }
    }
    fclose(ans);
    fclose(file);
    return 0;
}
