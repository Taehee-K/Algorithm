#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#include <queue>
using namespace std;

int main() {
	priority_queue<int> pq;//���� ���� �����ϴ� �켱���� ť
	int N, i, num;
	scanf("%d", &N);

	for (i = 0; i < N; i++) {
		scanf("%d", &num);//���� �Է� ����

		if (num != 0) //�Է� ���� 0�� �ƴ� ��-> �� ����
			pq.push(num);//�켱����ť�� �� �־���
		else if (pq.empty() == 1)//�Է� ���� 0�� �ƴ�, ť �������
			printf("0\n");//0���
		else {//�Է� ���� 0 �ƴ�-> �� ���
			printf("%d\n", pq.top());//���� ū ���� ���(�켱����)
			pq.pop();//���� ū �� ť���� ����
		}
	}
	return 0;
}