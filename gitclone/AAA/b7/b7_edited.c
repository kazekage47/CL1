// B7.C

#include <stdio.h>
#include <string.h>
#include <ctype.h>

char input[10];
int i,error;

void E();

void T();

void Eprime();

void Tprime();

void F();

main()
{
  i=0;
  error=0;
  printf("Enter an Arithmetic expression :");
  scanf("%s",&input[i]);
  E();
  if(strlen(input)==i&&error==0)
  {
    printf("Accepted \n");
  }
    else printf(" Rejected\n");
}



void E()
{
  T();
  Eprime();
}

void Eprime()
{

  if(input[i]=='+')
  {
    i++;
    T();
    Eprime();
  }
}


void T()
{
  F();
  Tprime();
}

void Tprime()
{
  if(input[i]=='*')
  {
    i++;
    F();
    Tprime();
  }
}
void F()
{
  if(isalnum(input[i]))i++;

  else if(input[i]=='(')
  {
    i++;
    E();

    if(input[i]==')')
    i++;
    else error=1;
  }

  else error=1;
}
