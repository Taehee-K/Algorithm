#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#include <queue>
using namespace std;

int main() {
	priority_queue<int> pq;//정수 값을 저장하는 우선순위 큐
	int N, i, num;
	scanf("%d", &N);

	for (i = 0; i < N; i++) {
		scanf("%d", &num);//정수 입력 받음

		if (num != 0) //입력 값이 0이 아닐 때-> 값 받음
			pq.push(num);//우선순위큐에 값 넣어줌
		else if (pq.empty() == 1)//입력 값이 0이 아님, 큐 비어있음
			printf("0\n");//0출력
		else {//입력 값이 0 아님-> 값 출력
			printf("%d\n", pq.top());//가장 큰 값을 출력(우선순위)
			pq.pop();//가장 큰 값 큐에서 제거
		}
	}
	return 0;
}