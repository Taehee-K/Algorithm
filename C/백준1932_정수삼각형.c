//[백준 1932/C] 정수삼각형

#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>

int a[501][501] = { 0 };	//숫자삼각형
int best[501][501] = { 0 };	//각 원소의 최적 경로값 저장하는 배열
int route[501] = { 0 };		//최적 경로 저장하는 삼각형

//a, b 값 중 더 큰 것 반환하는 함수
int MAX(int a, int b) {
	if (a > b)
		return a;
	else
		return b;
}

//정수삼각형에서의 최적 경로값을 저장하는 함수
int triangle(int n) {
	int i, j;
	int max = 0, index = 0, maxroute = 0;

	//a[][] 까지의 경로의 최대값을 best[][]에 저장한다. 
	for (i = 1; i <= n; i++) {
		for (j = 1; j <= i; j++) {
			//레벨 n까지의 각 자리의 원래 원소 값과 양쪽 위의 값들 중 더 큰 것 더함
			best[i][j] = a[i][j] + MAX(best[i - 1][j - 1], best[i - 1][j]);
		}
	}

	//n번째 레벨의 원소까지의 최적 경로값 중 최대값 구함
	for (i = 1; i <= n; i++) {
		if (max < best[n][i]) {
			max = best[n][i];	//최적 경로의 합 max에 저장
			index = i;	//최적 경로값을 가진 원소의 인덱스 저장
		}
	}

	for (i = 0; i < n; i++) {	//최적 경로 값으로부터 시작해서 경로 구하기
		if (i == 0) {	//최적 경로 값으로부터 시작
			route[n] = a[n][index];
		}
		else {	//최적 경로 삼각형을 거슬러 올라가면서(n-i) 경로 찾음 
			//각 원소 위의 두 개의 원소 중 큰 값으로 이동 
			maxroute = MAX(best[n - i][index - 1], best[n - i][index]);
			//왼쪽의 원소가 더 클 때 기준 인덱스 값을 하나 줄여준다. 
			if (maxroute == best[n - i][index - 1]) {
				route[n - i] = a[n - i][index - 1];
				index -= 1;
			}
			else
				route[n - i] = a[n - i][index];
		}
	}

	//최적 경로의 합 반환
	return max;
}

int main() {
	int n;
	int i, j;

	printf("1<=n<=500 의 정수 삼각형의 크기(최대 레벨) 'n'을 입력하세요: ");
	scanf("%d", &n);	//(1 ≤ n ≤ 500)인 삼각형의 크기 입력
	for (i = 1; i <= n; i++)
		for (j = 1; j <= i; j++)
			scanf("%d", &a[i][j]);	//n 번째 레벨까지 정수 삼각형 입력

	//정수삼각형의 최적 경로의 합 출력
	printf("최적 경로의 합: %d \n", triangle(n));

	////최적경로 삼각형 best[][] 출력(확인용)
	//for (i = 1; i <= n; i++) {
	//	for (j = 1; j <= i; j++) {
	//		printf("%d ", best[i][j]);
	//	}
	//	printf("\n");
	//}

	//정수삼각형의 최적 경로 출력
	for (i = 1; i <= n; i++) printf("%d ", route[i]);
}

