%{
    #include<stdio.h>
    #include<string.h>
    #include<stdlib.h>
	char AddtoTable(char ,char, char);
    void ThreeAddressCode();
    void Triple();
    void Qudraple();
    

    int index1=0;
    char temp='A';
    struct expr
    {
        char operand1;
        char operand2;
        char operator;
      };
%}

%union
{
    char symbol;
}

%token <symbol> LETTER NUMBER
%type <symbol> exp

%left '-''+'
%right '*''/'

%%

statement: LETTER '=' exp ';' {AddtoTable((char)$1,(char)$3,'=');}
           | exp ';'
       ;

exp: exp '+' exp {$$ = AddtoTable((char)$1,(char)$3,'+');}
      | exp '-' exp {$$ = AddtoTable((char)$1,(char)$3,'-');}
      | exp '*' exp {$$ = AddtoTable((char)$1,(char)$3,'*');}
      | exp '/' exp {$$ = AddtoTable((char)$1,(char)$3,'/');}
      | '(' exp ')' {$$ = (char)$2;}
      | NUMBER {$$ = (char)$1;}
      | LETTER {$$ = (char)$1;}
      ;

%%

yyerror(char *s)
{
  printf("%s",s);
  exit(0);
}

struct expr arr[20];
//int id=0;

char AddtoTable(char operand1,char operand2,char operator)
{
    arr[index1].operand1=operand1;
    arr[index1].operand2=operand2;
    arr[index1].operator=operator;
    index1++;
    temp++;
    return temp;
}

void ThreeAddressCode()
{
    int cnt=0;
    temp++;
    printf("\n\n\t THREE ADDRESS CODE\n\n");
    while(cnt<index1)
    {
        printf("%c : = \t",temp);  
        if(isalpha(arr[cnt].operand1))
            printf("%c\t",arr[cnt].operand1);
        else
            {printf("%c\t",temp);}
        printf("%c\t",arr[cnt].operator);
        if(isalpha(arr[cnt].operand2))
            printf("%c\t",arr[cnt].operand2);
        else
            {printf("%c\t",temp);}
        printf("\n");
        cnt++;
        temp++;
    }
}

void Quadraple()
{
    int cnt=0;
    char temp='A';
    temp++;
    printf("\n\n\t QUADRAPLE CODE\n\n");
	
    while(cnt<index1)
    {
        //printf("%d",id);
        //printf("\t");      
        printf("%c",arr[cnt].operator);
        printf("\t");   
            if(isalpha(arr[cnt].operand1))
                printf("%c\t",arr[cnt].operand1);
            else
                {printf("%c\t",temp);}  
            if(isalpha(arr[cnt].operand2))
                printf("%c\t",arr[cnt].operand2);
            else
                {printf("%c\t",temp);}      
            printf("%c",temp);
        printf("\n");
        cnt++;
        temp++;
      //  id++;  
    }
}



main()
{
    printf("\nEnter the Expression: ");
    yyparse();
    temp='A';
    ThreeAddressCode();
    Quadraple();
}

yywrap()
{
    return 1;
}

/*
### Output

[pict@localhost new_4403]$ ./a.out

Enter the Expression: x=((a+b)-(c/d))*m;


	 THREE ADDRESS CODE

B : = 	a	+	b	
C : = 	c	/	d	
D : = 	B	-	C	
E : = 	D	*	m	
F : = 	x	=	E	


	 QUADRAPLE CODE

0	+	a	b	H
1	/	c	d	I
2	-	B	C	J
3	*	D	m	K
4	=	x	E	L
[pict@localhost new_4403]$ 

k=l+m-n/a;
*/

