#include <stdio.h>
#include <stdlib.h>
#include <time.h>
int main(int a, char *aa[a])
{
    int A[1000128];
    FILE *file, *ans, *key;
    file = fopen(aa[2], "r");
    ans = fopen(aa[3], "w");
    key = fopen(aa[1], "r");
    int l;
    for (int i = 0; i < 127; i++)
    {
        fscanf(key, "%c", &l);
        A[i] = l - '0';
    }
    fclose(key);
    for (int i = 127; i < 1000128; i++)
    {
        A[i] = A[i - 1] ^ A[i - 127];
    }
    int index = 127, y = 0, x, B[8];
    char ascii[8];
    while (fgetc(file) != EOF)
    {
        fseek(file, -1, SEEK_CUR);
        for (int i = 0; i < 8; i++)
        {
            ascii[i] = fgetc(file);
        }
        for (int i = 0; i < 8; i++)
        {
            B[i] = ascii[i] - '0';
            B[i] = B[i]^A[index];
            index++;
        }
        int z = 0, pr = 128;
        for (int i = 0; i <= 7; i++)
        {
            z = z + pr*B[i];
            pr = pr/2;
        }
        fprintf(ans, "%c", z);
    }
    fclose(ans);
    fclose(file);
}

// index++;
// x = x - '0';
// B[y] = (x ^ A[index]);
// y++;
// if(y >= 8)
// {
//     y = 0;
//     z = 0;
//     for (int i = 0; i < 8; i++)
//     {
//         z = z + (pow(2, i)*B[i]);
//     }
//     fprintf(ans, "%c", z);
// }
// x = x - '0';
// for (int i = 0; i < 8; i++)
// {
//     int tempf = x & (1<<i);
//     B[i] = 0;
//     if(tempf) B[i] = 1;
// }
// for (int i = 7; i >= 0; i--)
// {
//     C[i] = A[index] ^ B[i];
//     index++;
// }
// int p = 0, k = 1;
// for (int i = 0; i < 8; i++)
// {
// }
// fprintf(ans, "%d", y);