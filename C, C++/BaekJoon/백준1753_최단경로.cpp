//[백준 1753/C++] 최단경로
//https://www.acmicpc.net/problem/1753

#define _CRT_SECURE_NO_WARNINGS
#include<cstdio>
#include <queue>
#include <vector>
using namespace std;

int INF = 1000000000;
int V, E, start;//V:정점의 수, E:간선의 수, start:시작 정점의 번호
int dist[20001];//시작점으로부터의 거리
vector<pair<int, int>> weight[20001];  //가중치 그래프

void dijkstra() {

    for (int i = 1; i <= V; i++)    //초기화
        dist[i] = INF;//각 점에서의 거리 INF로 초기화
    dist[start] = 0;//시작점에서의 거리 0

    //pair<weight, vertex> 우선순위 큐 생성 
    //오름차순으로 정렬(최솟값 찾기)위해 greater 비교연산자 사용
    priority_queue<pair<int, int>, vector<pair<int, int>>, greater<pair<int, int>>>pq;
    pq.push({ 0, start });//시작 점에서의 거리는 0;

    while (!pq.empty()) {//우선 순위 큐가 비어있지 않는 한
        int length = pq.top().first;    //큐에 있는 값 중 최단 경로
        int node = pq.top().second;  //현재 정점
        pq.pop();//최솟값(최단거리) 제거

        //현재까지의 거리가 새로 얻은 가중치보다 작을 때 넘어가기
        if (dist[node] < length) continue;

        int nodeNum = weight[node].size(); //남아있는 정점들의 수 
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

    //V개의 정점, E 개의 간선의 개수 입력 받기
    scanf("%d %d", &V, &E);
    //시작 정점의 번호 K 입력 받기
    scanf("%d", &start);

    //거리 초기화
    for (int i = 0; i < V; i++)
        dist[i] = INF;

    //버스의 출발지, 도착지에 해당하는 비용 입력받기
    while (E--) {
        int u, v, w;
        //u->v 로 가는 가중치를 입력받아 저장한다. 
        scanf("%d %d %d", &u, &v, &w);
        weight[u].push_back({ v, w });
    }

    dijkstra();
    return 0;
}