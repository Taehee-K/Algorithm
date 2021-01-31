#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>

int arr[1001] = { 0 };  //n 개의 정수가 저장된 배열
int h[1001] = { 0 };    //부분 수열의 길이
int p[1001] = { 0 };    //전 값의 인덱스
int list[1001] = { 0 }; //최장 증가 부분 수열

int main() {
    int N;  //정수 수열의 크기  
    int index=0, i, j;
    int max = 0;    //부분 수열의 최대 길이

    printf("1이상, 1000이하의 길이인 정수 수열의 크기를 입력하시오: ");
    scanf("%d", &N);    //크기(1<=N<=1000)인 수열 A

    printf("수열 A를 이루고 있는 정수들을 입력하세요: ");
    arr[0] = -100;
    for (i = 1; i < N + 1; i++) {
        h[i] = 1;
        scanf("%d", &arr[i]);   //수열 A 이루고 있는 Ai(1<=Ai<=1000)
        for (j = 0; j < i; j++) {
            //수열 값이 더 작을 것들 중 증가부분수열의 길이가 가장 긴 것 구함
            if (arr[i] > arr[j] && h[i] < h[j] + 1) {
                h[i] = h[j] + 1;    //증가부분수열의 길이 저장
                p[i] = j;   //전 원소의 인덱스 저장 
            }
        }

        if (max < h[i]) {   //부분수열의 길이(h)가 가장 긴 것으로 갱신 
            max = h[i];
            index = i;  //최대길이를 저장한 인덱스 값 
        }
    }

    i = max;
    while (index != 0) {    //index == 0 일 때까지 반복
        i -= 1; //최장증가수열 인덱스 감소 -> 가장 큰 수 부터 거꾸로 저장함
        list[i] = arr[index];   //최장증가수열에 해당하는 수 list[]에 넣어줌
        index = p[index];       //인덱스 업데이트-> 최단 경로의 이전 수로 가게끔 함
    }

    //수열 A의 가장 긴 증가하는 부분수열의 길이를 출력
    printf("longest increasing subsequence length: %d \n", max);
    printf("longest increasing subsequence: "); //가장 긴 증가하는 부분 수열 출력 
    for (i = 0; i < max; i++) printf("%d ", list[i]);
}
