#include <stdio.h>


int main(){
	char choice;
	int a,b,loop=1;
	printf("Simple calculator program\n");
	
	printf("Enter first number : ");
	scanf("%d",&a);
	
	while(loop=1){



		
		
		printf("\n\t\tOperations");
		printf("\n\t\t+");
		printf("\n\t\t-");
		printf("\n\t\t*");
		printf("\n\t\t/");
		printf("\n\t\tq (quit)");
		printf("\n\t\tc (clear)\n:");
		scanf("%c",&choice);
	
		printf("\nEnter next number : ");
		scanf("%d",&b);
		
		switch(choice){
			case '+':
				a+=b;

			case '-':
				a-=b;

			case '*':
				a*=b;

			case '/':
				a/=b;

			case 'q':
				loop = 0;

			case 'c':
				a = 0;
				
		
		printf("Result : %d",a);
		};
	}
}	
