#define _CRT_SECURE_NO_WARNINGS
#include<stdio.h>

double Fac(int a)
{
	double result = 1;
	for (int i = 1; i <= a; i++)
	{
		result = result * i;
	}
	return result;
}

int main(void)
{
	int T;
	scanf("%d", &T);


	for (int i = 0; i < T; i++)
	{
		int k, n;
		scanf("%d %d", &k, &n);

		if (1 <= k && k <= 14)
		{
			if (1 <= n && n <= 14)
			{
				printf("%.0lf\n", Fac(k + n) / (Fac(n - 1) * Fac(k + 1)));
			}
			else
			{
				break;
			}	
		}
		else
		{
			break;
		}

		
	}
	return 0;
	
}