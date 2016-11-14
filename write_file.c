#include <stdio.h>

void main(){

	char ch[1000];
	FILE *file;

	file = fopen("data_files/write", "w");


	if ( file ) {
		
		printf("Enter a sentence");
		scanf("%[^\n]s",ch); //Scans till new line encountered
		
		fprintf(file, "%s" , ch );

		fclose(file);
		
		}

		




	else printf( "File doesnot Exist" );

}
                                                                              
                                                                               
                                                                               
                                                                               
             