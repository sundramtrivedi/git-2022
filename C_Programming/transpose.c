#include<stdio.h>
int main()
{
	int a[3][3];
	int trans[3][3];
	// enter the input
	printf("\n Enter matrix elements : \n");
	for(int i=0;i<3;++i)
	{
		for(int j=0;j<3;++j)
		{
			printf("\n Enter the metrix a[%d][%d] :",i,j);
			scanf("%d",&a[i][j]);
		}
	}
	// printing the matrix
	printf("\n Entered matrix elements : \n");
	for(int i=0;i<3;++i)
	{
		for(int j=0;j<3;++j)
		{
			printf("\n Enter the metrix a[%d][%d] : %d",i,j,a[i][j]);
		}
	}
	// computing transpose
	for(int i=0;i<3;++i)
	{
		for(int j=0;j<3;++j)
		{
			trans[j][i] = a[i][j];
			printf("\n Transpose the metrix trans[%d][%d] : %d",i,j,trans[j][i]);
		}
	}
	// printing transpose matrix
	printf("\n Transpose matrix elements : \n");
	for(int i=0;i<3;++i)
	{
		for(int j=0;j<3;++j)
		{
			printf("\n Transpose the metrix trans[%d][%d] : %d",i,j,trans[j][i]);
		}
	}
	return 0;
}
