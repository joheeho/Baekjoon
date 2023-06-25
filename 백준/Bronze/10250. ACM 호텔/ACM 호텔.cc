#include <stdio.h>

int main()
{
    int t, h, w, n;
    
    scanf("%d", &t);
    
    for (int i = 0; i < t; i++)
    {
        scanf("%d %d %d", &h, &w, &n);
        
        int x = (n - 1) % h + 1;  // 층 수 계산
        int y = (n - 1) / h + 1;  // 호 수 계산
        
        printf("%d%02d\n", x, y);
    }
    
    return 0;
}
