#include <stdio.h>

void hello(char* s){
	printf("Hello %s \n", s);
}

void chao(char* s){
	printf("Chao %s \n", s);
}

void bonjour(char* s){
	printf("Bonjour %s \n", s);
}

int main(){
	hello("Thanh An");
	chao("Thanh An");
	bonjour("Thanh An");
}
