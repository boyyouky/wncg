#include"stdafx.h"
#include"string.h"
#include"stdio.h"
#define MAXNUM 200
#define TRUE 1
#define FALSE 0
typedef struct
{
	char name[20];
	char telno[20];
}TelRecord;
typedef struct
{
	TelRecord records[MAXNUM];
	int last;
}SqTelPad;
void AddRecord(SqTelPad &telPad);
void DeleteRecord(SqTelPad &telPad);
void DispRecord(SqTelPad &telPad);
void InitSqTelPad(SqTelPad &telPad);

void main()
{
	char selectiem[5];
	int refreshflag;
	SqTelPad mytelpad;
	refreshflag = FALSE;
	InitSqTelPad(mytelpad);
	do
	{
		printf("*****************************\n");
		printf("*                           *\n");
		printf("*telephone   notepad        *\n");
		printf("*                           *\n");
		printf("*****************************\n");
		printf("1.add         record         \n");
		printf("2.delete      record         \n");
		printf("3.display     record         \n");
		printf("4.exit                       \n");
		scanf("%s",selectiem[0]);
		while(selectiem[0])
		{
			switch(selectiem[0])
			{case '1':
				AddRecord(mytelpad);
				refreshflag = TRUE;
				break;
			case '2':
				DeleteRecord(mytelpad);
				refreshflag =TRUE;
				break;
			case '3':
				DispRecord(mytelpad);
				refreshflag =TRUE;
				break;
			case '4':
				return;
			}
			if(refreshflag==TRUE)
			{
				refreshflag =FALSE;
			break;
			}
			else
			{
				scanf("%s",selectiem);
			}
		}
	}while(1);
}
void AddRecord(SqTelPad &telPad)
{	int n;
	telPad.last++;
	n = telPad.last;
	printf("please input new content\n");
	scanf("%s%s",telPad.records[n].name,telPad.records[n].telno);
}
void DeleteRecord(SqTelPad &telPad)
{
	int i,j;
	char name[20];
	printf("please input deleted new you want\n");
	scanf("%s",name);
	i =j =0;
	for(i = 0,i<=telPad.last;i++)
	{if(strcmp(telPad.records[i].name,name)==0){break;}}
	if(i>telPad.last)
	{
		printf("no record\n");
		return;
	}
	for(j=i;j<telPad.last;j++)
	{
		telPad.records[j] = telPad.records[j+1];
		telPad.last--;
	}
}
void DispRecord(SqTelPad &telPad)
{
	int i;
	for(i=0;i<=telPad.last;i++)
		printf("%s,%s\n",telPad.records[i].name,telPad.records[i].telno);
}
void InitSqTelPad(SqTelPad &telPad)
{telPad.last == -1;
}
			