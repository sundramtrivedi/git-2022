#include <stdio.h>
#include <stdlib.h>
#include <ctype.h>
#define ROWS 3
#define COLUMNS 5

/* prototypes */
void explainProg(void);
void DisplayMenu(void);
void LeftToRightDiagonal(void);
void OriginalArray(int recArray[][COLUMNS]);
void addRows(int recArray[][COLUMNS],int Sum[]);
void addColumns(int recArray[][COLUMNS],int Sum[]);

/* driver code */
int main(void){
    explainProg();
    DisplayMenu();
    return 0;
}

/* calling desired functions inside it */
void explainProg(void){
    puts("\n\n\n\tThis program will 1st fill the left-to-right diagonal of a matrix ,\n\t2nd find the sum of each row and coumn of a given matrix.\n");
    system("pause");
    system("cls");
    return;
}

/* to display the menu */
void DisplayMenu(void){
    char Choice;
    /* actual array */
    int originalArray[3][5]= {{ 10, 21,30,39,50 },
                                { 15,33,41,10,42 },
                                { 16,18,64,20,12 }};
    int sumRow[ROWS];
    int sumCol[COLUMNS];
  
    do{
        printf("\nMenu:\n");
        printf("a. Fill the left to right diagonal of a matrix\n");
        printf("b. Print the original array\n");
        printf("c. Find the sum of each row\n");
        printf("d. Find the sum of each column\n");
        printf("\t\t\tx) Exit\n");
        printf("\n\t\t\tPlease enter your choice: ");
        scanf(" %c",&Choice);
        Choice = toupper(Choice);
    
        /* to choose among the options */
        switch(Choice)
        {
            case'A': 
                LeftToRightDiagonal();
                break;
            case'B':
                OriginalArray(originalArray);
                break;
            case'C':
                addRows(originalArray, sumRow);
                break;
            case'D':
                addColumns(originalArray, sumCol);
                break;
            case'X':
                printf("\n\t\tExiting\n\n"); 
                exit(0);
                break;
            default:
                printf("\t\t\tInvalid Choice\n\n");
                break;
        }
        system("pause");
        system("cls");
    } while(Choice != 'x');
    return;
}

/* filling the matrix */
void LeftToRightDiagonal(void){
    int array[6][6];
    int row;
    int col;
    for(row = 0; row < 6; row++){
        for(col = 0; col < 6; col++){
            if(row < col){
                array[row][col] =1;
            }
            else if (row > col){
                array[row][col] =-1;
            }
            else if (row == col){
                array[row][col] =0;
            }
        }
    }

    for(row = 0; row < 6; row++){
        for(col = 0; col < 6; col++){
            printf("%d\t",array[row][col]);
        }
        printf("\n");
    }
}

/* displaying the actual array */
void OriginalArray(int recArray[ROWS][COLUMNS]){
    int rows;
    int columns;
    printf("\n\nThis is the original array:\n\n");
    for(rows = 0; rows < 3; rows++){
        for(columns = 0; columns < 5; columns++){
            printf(" %d", recArray[rows][columns]);
        }
        printf("\n\n");
    }
}

/* finding the sum of elements in each row */
void addRows(int recArray[ROWS][COLUMNS], int Sum[]){
    int rows;
    int columns;
    for(rows = 0; rows < ROWS; rows++)
    {
        Sum[rows]= 0;
        for(columns = 0; columns < COLUMNS; columns++)
        {
            Sum[rows]= Sum[rows]+ recArray[rows][columns];
        }
    }
    for(rows = 0; rows < 3; rows++)
        printf("The sum of rows %d is %d\n", rows, Sum[rows]);
    printf("\n");
}

/* finding the sum of elements in each column */
void addColumns(int recArray[ROWS][COLUMNS], int Sum[]){
    int rows;
    int columns;
    for(columns = 0; columns < COLUMNS; columns++)
    {
        Sum[columns]= 0;
        for(rows = 0; rows < ROWS; rows++)
        {
            Sum[columns]= Sum[columns]+ recArray[rows][columns];
        }
    }
    for(columns = 0; columns < 5; columns++)
    printf("The sum of columns %d is %d\n", columns, Sum[columns]);
    printf("\n");
    system("pause");
}