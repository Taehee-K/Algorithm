//[백준 10828/C++] 스택
//https://www.acmicpc.net/problem/10828

#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#include <string.h>
#include <stack>
using namespace std;

int main() {
	stack<int> stk; //정수 담는 stk 스택 생성
	int N, i, n;
	char a[100];
	scanf("%d", &N);

	for (i = 0; i < N; i++) {
		scanf("%s", a); //명령어 입력 받아 a 배열에 저장

		if (strcmp(a, "push") == 0) {//명령어가 push
			scanf("%d", &n);//입력 받은 정수 스택에 집어넣음
			stk.push(n);
		}
		if (strcmp(a, "top") == 0) {//명령어가 top
			if (stk.empty() == 1)//스택 비어 있을 때
				printf("-1\n");	//-1 출력
			else //스택 비어 있지 않을 떄 
				printf("%d\n", stk.top());	//스택의 맨 위에 있는 값 출력
		}

		if (strcmp(a, "size") == 0)	//스택에 몇 개가 있는지 출력
			printf("%d\n", stk.size());

		if (strcmp(a, "empty") == 0) //스택 비어 있는지 출력
			printf("%d\n", stk.empty());

		if (strcmp(a, "pop") == 0) {	//스택 값 pop
			if (stk.empty() == 1)	//스택 비어 있으면 -1 출력
				printf("-1\n");
			else {
				printf("%d\n", stk.top());	//스택 맨 위의 값 뽑으면서 출력
				stk.pop();	//스택 맨 위의 값 없애줌
			}
		}
	}
	return 0;
}