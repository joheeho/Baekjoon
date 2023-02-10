#include <stdio.h>
#include <stdlib.h>
#include <string.h>


typedef struct
{
	int num;
	char name[21];
}pokemon;

int cmp(const void* a, const void* b)
{
	pokemon *na = (pokemon*)a;
	pokemon *nb = (pokemon*)b;
	if (strcmp(na->name, nb->name) > 0)
        return 1;
    else
        return -1;
}

int main(void)
{
	int n, m,i;
    pokemon* pokemon_index= NULL;
    pokemon* pokemon_index_C = NULL;
	char op[21];
    scanf("%d %d", &n, &m);

	pokemon_index   = (pokemon*)malloc(sizeof(pokemon) * n);
	pokemon_index_C = (pokemon*)malloc(sizeof(pokemon) * n);

	for (int i = 0; i < n; i++)
	{
		scanf("%s", pokemon_index[i].name);
		pokemon_index[i].num = pokemon_index_C[i].num = i + 1;
		pokemon_index_C[i] = pokemon_index[i];
	}

	qsort(pokemon_index_C, n, sizeof(pokemon_index_C[0]), cmp);

	for (i = 0; i < m; i++)
	{
		scanf("%s", op);

		if (op[0] >= '0' && op[0] <= '9')
		{
			int num1 = atoi(op);
			printf("%s\n", pokemon_index[num1 - 1].name);
		}
		else
		{
            int mid;
			int low = 0, high = n - 1;
			while (low <= high)
			{
                mid = (low + high) / 2;
				if (strcmp(pokemon_index_C[mid].name, op) == 0)
				{
                    printf("%d\n", pokemon_index_C[mid].num);
					break;
				}
				else if (strcmp(pokemon_index_C[mid].name, op) > 0)
				{
					high = mid - 1;
				}
				else
				{
					low = mid + 1;
				}
			}
		}
	}

	free(pokemon_index);
	free(pokemon_index_C);

	return 0;
}