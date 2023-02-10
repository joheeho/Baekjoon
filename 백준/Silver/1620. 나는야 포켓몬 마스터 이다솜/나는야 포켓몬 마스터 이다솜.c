#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <ctype.h>

typedef struct Poketmonster // 포켓 몬스터 구조체를 만들기
{
	int num;
	char name[21];
} Poketmonster;

Poketmonster secondary_list[100000][21];  
Poketmonster sorted_secondary_list[100000][21];

int compare(const void* A, const void* B)
{
	Poketmonster* a = (Poketmonster*)A;
	Poketmonster* b = (Poketmonster*)B;

	return strcmp(a->name, b->name);
}

int main()
{
	int n, m;

	char tmp_name[21];
	Poketmonster command;

	scanf("%d %d", &n, &m);

	for (int i = 0; i < n; i++)
	{
		scanf("%s", tmp_name);
		strcpy(secondary_list[i]->name, tmp_name);
		strcpy(sorted_secondary_list[i]->name, tmp_name);
		secondary_list[i]->num = i;
		sorted_secondary_list[i] ->num = i;
	}

	qsort(sorted_secondary_list, n, sizeof(sorted_secondary_list[0]), compare);

	for (int i = 0; i < m; i++)
	{
		scanf("%s", command.name);
		if (isdigit(command.name[0]))
			printf("%s\n", secondary_list[atoi(command.name) - 1]->name);
		else
		{
			Poketmonster* monster = (Poketmonster*)bsearch(&command, sorted_secondary_list, n, sizeof(sorted_secondary_list[i]), compare);
			printf("%d\n", monster->num + 1);
		}
	}
	return 0;
}