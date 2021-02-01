//[���� 1753/C++] �ִܰ��
//https://www.acmicpc.net/problem/1753

#define _CRT_SECURE_NO_WARNINGS
#include<cstdio>
#include <queue>
#include <vector>
using namespace std;

int INF = 1000000000;
int V, E, start;//V:������ ��, E:������ ��, start:���� ������ ��ȣ
int dist[20001];//���������κ����� �Ÿ�
vector<pair<int, int>> weight[20001];  //����ġ �׷���

void dijkstra() {

    for (int i = 1; i <= V; i++)    //�ʱ�ȭ
        dist[i] = INF;//�� �������� �Ÿ� INF�� �ʱ�ȭ
    dist[start] = 0;//������������ �Ÿ� 0

    //pair<weight, vertex> �켱���� ť ���� 
    //������������ ����(�ּڰ� ã��)���� greater �񱳿����� ���
    priority_queue<pair<int, int>, vector<pair<int, int>>, greater<pair<int, int>>>pq;
    pq.push({ 0, start });//���� �������� �Ÿ��� 0;

    while (!pq.empty()) {//�켱 ���� ť�� ������� �ʴ� ��
        int length = pq.top().first;    //ť�� �ִ� �� �� �ִ� ���
        int node = pq.top().second;  //���� ����
        pq.pop();//�ּڰ�(�ִܰŸ�) ����

        //��������� �Ÿ��� ���� ���� ����ġ���� ���� �� �Ѿ��
        if (dist[node] < length) continue;

        int nodeNum = weight[node].size(); //�����ִ� �������� �� 
        for (int i = 0; i < nodeNum; i++) {
            int next_node = weight[node][i].first;
            int next_length = length + weight[node][i].second;

            if (dist[next_node] > next_length) {
                dist[next_node] = next_length;
                pq.push({ next_length, next_node });
            }
        }
    }

    for (int i = 1; i <= V; i++) {
        if (start == i) printf("0\n");
        else if (dist[i] == INF) printf("INF\n");
        else printf("%d\n", dist[i]);
    }
}

int main() {

    //V���� ����, E ���� ������ ���� �Է� �ޱ�
    scanf("%d %d", &V, &E);
    //���� ������ ��ȣ K �Է� �ޱ�
    scanf("%d", &start);

    //�Ÿ� �ʱ�ȭ
    for (int i = 0; i < V; i++)
        dist[i] = INF;

    //������ �����, �������� �ش��ϴ� ��� �Է¹ޱ�
    while (E--) {
        int u, v, w;
        //u->v �� ���� ����ġ�� �Է¹޾� �����Ѵ�. 
        scanf("%d %d %d", &u, &v, &w);
        weight[u].push_back({ v, w });
    }

    dijkstra();
    return 0;
}