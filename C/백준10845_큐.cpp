//[백준 10845/C++] 큐

#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#include <string.h>
#include <queue>
using namespace std;

int main() {
	queue<int> q; //정수 값을 입력 받는 큐 생성
	int N, i, n;
	char a[100]; //명령어 받을 배열
	scanf("%d", &N);

	for (i = 0; i < N; i++) {
		scanf("%s", a); //명령어 읽어들임

		if (strcmp(a, "push") == 0) {//push 명령어
			scanf("%d", &n);//읽어들인 값
			q.push(n);//큐에 집어 넣음
		}
		if (strcmp(a, "front") == 0) {//front 명령어
			if (q.empty() == 1)//큐가 비어있으면
				printf("-1\n");//-1 출력
			else//큐가 비어있지 않으면
				printf("%d\n", q.front());//맨 앞의 값을 출력
		}
		if (strcmp(a, "back") == 0) {//back 명령어
			if (q.empty() == 1)//큐가 비어있을 때
				printf("-1\n");//-1 출력
			else//큐가 비어있지 않으면
				printf("%d\n", q.back());//맨 뒤의 값을 출력
		}
		if (strcmp(a, "size") == 0)//size 명령어
			printf("%d\n", q.size());//큐의 크기 출력

		if (strcmp(a, "empty") == 0)//empty 명령어
			printf("%d\n", q.empty());//큐가 비었있는지 상태 출력

		if (strcmp(a, "pop") == 0) {//pop 명령어
			if (q.empty() == 1)//큐가 비어 있을 때 
				printf("-1\n");//-1 출력
			else {//큐가 비어있지 않을 떄
				printf("%d\n", q.front());//맨 앞의 값 출력
				q.pop();//맨 앞의 값 삭제해줌
			}
		}
	}
}