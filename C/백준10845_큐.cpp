//[���� 10845/C++] ť

#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#include <string.h>
#include <queue>
using namespace std;

int main() {
	queue<int> q; //���� ���� �Է� �޴� ť ����
	int N, i, n;
	char a[100]; //��ɾ� ���� �迭
	scanf("%d", &N);

	for (i = 0; i < N; i++) {
		scanf("%s", a); //��ɾ� �о����

		if (strcmp(a, "push") == 0) {//push ��ɾ�
			scanf("%d", &n);//�о���� ��
			q.push(n);//ť�� ���� ����
		}
		if (strcmp(a, "front") == 0) {//front ��ɾ�
			if (q.empty() == 1)//ť�� ���������
				printf("-1\n");//-1 ���
			else//ť�� ������� ������
				printf("%d\n", q.front());//�� ���� ���� ���
		}
		if (strcmp(a, "back") == 0) {//back ��ɾ�
			if (q.empty() == 1)//ť�� ������� ��
				printf("-1\n");//-1 ���
			else//ť�� ������� ������
				printf("%d\n", q.back());//�� ���� ���� ���
		}
		if (strcmp(a, "size") == 0)//size ��ɾ�
			printf("%d\n", q.size());//ť�� ũ�� ���

		if (strcmp(a, "empty") == 0)//empty ��ɾ�
			printf("%d\n", q.empty());//ť�� ����ִ��� ���� ���

		if (strcmp(a, "pop") == 0) {//pop ��ɾ�
			if (q.empty() == 1)//ť�� ��� ���� �� 
				printf("-1\n");//-1 ���
			else {//ť�� ������� ���� ��
				printf("%d\n", q.front());//�� ���� �� ���
				q.pop();//�� ���� �� ��������
			}
		}
	}
}