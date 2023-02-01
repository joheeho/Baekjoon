#define _CRT_SECURE_NO_WARNINGS
#include<stdio.h>
#define minF(a,b) a<b?a:b

int main(void)
{
	char arr[50][50] = {};
	int n, m;
	scanf("%d %d", &n, &m);
	int min = 80;

	for (int i = 0; i < n; i++) {
    scanf("%s", arr[i]);
   }

	for (int a = 0; a+7 < n; a++) {
		for (int b = 0; b+7 < m; b++) {
			int black_first = 0;
			int white_first = 0;
			for (int i = a; i < a + 8; i++) {
				for (int j = b; j < b + 8; j++) {
					if ((i + j) % 2 == 0) {
						if (arr[i][j] == 'B') {
							white_first++;
						}
						else {
							black_first++;
						}
					}
					else {
						if (arr[i][j] == 'B') {
							black_first++;
						}
						else {
							white_first++;
						}
					}
				}
			}
			min = minF(min, black_first);
			min = minF(min, white_first);
			}
		}
	printf("%d",min);
}