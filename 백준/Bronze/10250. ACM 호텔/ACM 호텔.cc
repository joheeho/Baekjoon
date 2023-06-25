#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>

int t, h, w, n;

int main()
{
    scanf("%d", &t);

    for (int i = 0; i < t; i++)
    {
        scanf("%d %d %d", &h, &w, &n);

        int x = (n - 1) / h + 1; // x 좌표 계산
        int y = (n - 1) % h + 1; // y 좌표 계산

        printf("%d%02d\n", y, x);
    }

    return 0;
}
