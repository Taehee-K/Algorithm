//[���� 1916/C++] �ּҺ��

#define _CRT_SECURE_NO_WARNINGS
#include<cstdio>
using namespace std;

int INF = 987654321;
int N, M;   //n: ������ ����, m: ������ ����
int start, dest; //start: ��� ����, dest: ���� ����
int weight[1001][1001];
int length[1001];
bool check[1001];

void dijkstra() {
    int vnear;

    for (int i = 1; i <= N; i++)    //�ʱ�ȭ
        length[i] = weight[start][i];   //���������� ����ġ ��¡
    check[start] = true;    //���� ���� �̹� ���õǾ� ���� -> true

    for (int k = 1; k < N - 1; k++) {   //n-1���� ������ ���ʷ� �߰�
        int min = INF;  //�ּڰ� ó���� �� �ſ� ū ���� ����
        for (int i = 1; i <= N; i++)
            //���� ���õ��� ���� ������ ����ġ�� ��������� �ּڰ����� ���� ��
            if (check[i] == false && min > length[i]) {
                min = length[i];    //�ּڰ� ����
                vnear = i; //�ּڰ��� ���� �Ǵ� ������ �ε��� ����
            }

        check[vnear] = true; //�ּڰ��� ���� �Ǵ� ���� ���� -> true

        for (int i = 1; i <= N; i++) {
            //���� ���õ��� ���� �����鿡 ���� length[i] ����
            if (check[i] == false && length[i] > length[vnear] + weight[vnear][i]) {
                length[i] = length[vnear] + weight[vnear][i];
            }
        }
    }
}

int main() {
    //N���� ���� ��, M���� ���� �� �Է� �ޱ�
    scanf("%d %d", &N, &M);

    //����ġ �׷��� �ʱ�ȭ�ϱ�
    for (int i = 1; i <= N; i++) {
        for (int j = 1; j <= N; j++) {
            if (i == j) weight[i][j] = 0;	//����� = �������϶� ��� 0
            else weight[i][j] = INF;	//��� ������ �� ������ �ִٰ� ����(��� �ִ�)
        }
    }

    //������ �����, �������� �ش��ϴ� ��� �Է¹ޱ�
    while (M--) {
        int from, to, fee;
        scanf("%d %d %d", &from, &to, &fee);
        if (weight[from][to] > fee)
            weight[from][to] = fee;
    }

    //�ּ� ����� ���Ϸ��� ��� ���ÿ� ���� ���� �Է� �ޱ�
    scanf("%d %d", &start, &dest);

    //���ͽ�Ʈ�� �˰��� ���� �ּ� ��� ���ϱ�
    dijkstra();

    //start-> dest�� �ּ� ��� ���
    printf("%d\n", length[dest]);

    return 0;
}