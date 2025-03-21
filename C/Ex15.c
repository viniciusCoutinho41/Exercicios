#include <stdio.h>
#include "boolean.h"

int main() {
	//Atividade 05.2
	
	printf("%s ", bool(not false) );
	printf("%s ", bool(false and true) );
	printf("%s ", bool(true or false) );

	return 0;
}