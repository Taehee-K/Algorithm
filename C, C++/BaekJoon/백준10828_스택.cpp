//[���� 10828/C++] ����
//https://www.acmicpc.net/problem/10828

#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#include <string.h>
#include <stack>
using namespace std;

int main() {
	stack<int> stk; //���� ��� stk ���� ����
	int N, i, n;
	char a[100];
	scanf("%d", &N);

	for (i = 0; i < N; i++) {
		scanf("%s", a); //��ɾ� �Է� �޾� a �迭�� ����

		if (strcmp(a, "push") == 0) {//��ɾ push
			scanf("%d", &n);//�Է� ���� ���� ���ÿ� �������
			stk.push(n);
		}
		if (strcmp(a, "top") == 0) {//��ɾ top
			if (stk.empty() == 1)//���� ��� ���� ��
				printf("-1\n");	//-1 ���
			else //���� ��� ���� ���� �� 
				printf("%d\n", stk.top());	//������ �� ���� �ִ� �� ���
		}

		if (strcmp(a, "size") == 0)	//���ÿ� �� ���� �ִ��� ���
			printf("%d\n", stk.size());

		if (strcmp(a, "empty") == 0) //���� ��� �ִ��� ���
			printf("%d\n", stk.empty());

		if (strcmp(a, "pop") == 0) {	//���� �� pop
			if (stk.empty() == 1)	//���� ��� ������ -1 ���
				printf("-1\n");
			else {
				printf("%d\n", stk.top());	//���� �� ���� �� �����鼭 ���
				stk.pop();	//���� �� ���� �� ������
			}
		}
	}
	return 0;
}