//[���� 1932/C] �����ﰢ��

#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>

int a[501][501] = { 0 };	//���ڻﰢ��
int best[501][501] = { 0 };	//�� ������ ���� ��ΰ� �����ϴ� �迭
int route[501] = { 0 };		//���� ��� �����ϴ� �ﰢ��

//a, b �� �� �� ū �� ��ȯ�ϴ� �Լ�
int MAX(int a, int b) {
	if (a > b)
		return a;
	else
		return b;
}

//�����ﰢ�������� ���� ��ΰ��� �����ϴ� �Լ�
int triangle(int n) {
	int i, j;
	int max = 0, index = 0, maxroute = 0;

	//a[][] ������ ����� �ִ밪�� best[][]�� �����Ѵ�. 
	for (i = 1; i <= n; i++) {
		for (j = 1; j <= i; j++) {
			//���� n������ �� �ڸ��� ���� ���� ���� ���� ���� ���� �� �� ū �� ����
			best[i][j] = a[i][j] + MAX(best[i - 1][j - 1], best[i - 1][j]);
		}
	}

	//n��° ������ ���ұ����� ���� ��ΰ� �� �ִ밪 ����
	for (i = 1; i <= n; i++) {
		if (max < best[n][i]) {
			max = best[n][i];	//���� ����� �� max�� ����
			index = i;	//���� ��ΰ��� ���� ������ �ε��� ����
		}
	}

	for (i = 0; i < n; i++) {	//���� ��� �����κ��� �����ؼ� ��� ���ϱ�
		if (i == 0) {	//���� ��� �����κ��� ����
			route[n] = a[n][index];
		}
		else {	//���� ��� �ﰢ���� �Ž��� �ö󰡸鼭(n-i) ��� ã�� 
			//�� ���� ���� �� ���� ���� �� ū ������ �̵� 
			maxroute = MAX(best[n - i][index - 1], best[n - i][index]);
			//������ ���Ұ� �� Ŭ �� ���� �ε��� ���� �ϳ� �ٿ��ش�. 
			if (maxroute == best[n - i][index - 1]) {
				route[n - i] = a[n - i][index - 1];
				index -= 1;
			}
			else
				route[n - i] = a[n - i][index];
		}
	}

	//���� ����� �� ��ȯ
	return max;
}

int main() {
	int n;
	int i, j;

	printf("1<=n<=500 �� ���� �ﰢ���� ũ��(�ִ� ����) 'n'�� �Է��ϼ���: ");
	scanf("%d", &n);	//(1 �� n �� 500)�� �ﰢ���� ũ�� �Է�
	for (i = 1; i <= n; i++)
		for (j = 1; j <= i; j++)
			scanf("%d", &a[i][j]);	//n ��° �������� ���� �ﰢ�� �Է�

	//�����ﰢ���� ���� ����� �� ���
	printf("���� ����� ��: %d \n", triangle(n));

	////������� �ﰢ�� best[][] ���(Ȯ�ο�)
	//for (i = 1; i <= n; i++) {
	//	for (j = 1; j <= i; j++) {
	//		printf("%d ", best[i][j]);
	//	}
	//	printf("\n");
	//}

	//�����ﰢ���� ���� ��� ���
	for (i = 1; i <= n; i++) printf("%d ", route[i]);
}

