#include <stdio.h>
#include <math.h>


int CheckPrime(int num){
	int i;
	int squarenum = sqrt(num);
	if(num==2) return 1;
	if(num%2==0)return 0;

	//If a number is not divisible by 2, then it will not be divisible by any other even number.
	
	for(i=2 ; i<=squarenum ; i+=2){		//If n is not a prime, atleast one of its factors will be equal to or less than root of that number 
		if( num%i==0 ) return 0;
	
	}

	return 1;
	
}


void main(){

	int num;

	printf("Enter your number : ");
	scanf("%d",&num);
	
	if (CheckPrime(num)==0) printf("Number is not a prime. \n");
	else printf("Number is a prime. \n");
}
