//[백준 1916/C++] 최소비용

#define _CRT_SECURE_NO_WARNINGS
#include<cstdio>
using namespace std;

int INF = 987654321;
int N, M;   //n: 도시의 개수, m: 버스의 개수
int start, dest; //start: 출발 도시, dest: 도착 도시
int weight[1001][1001];
int length[1001];
bool check[1001];

void dijkstra() {
    int vnear;

    for (int i = 1; i <= N; i++)    //초기화
        length[i] = weight[start][i];   //시작점과의 가중치 저징
    check[start] = true;    //시작 노드는 이미 선택되어 있음 -> true

    for (int k = 1; k < N - 1; k++) {   //n-1개의 정점을 차례로 추가
        int min = INF;  //최솟값 처음에 값 매우 큰 수로 설정
        for (int i = 1; i <= N; i++)
            //아직 선택되지 않은 정점의 가중치가 현재까지의 최솟값보다 작을 때
            if (check[i] == false && min > length[i]) {
                min = length[i];    //최솟값 갱신
                vnear = i; //최솟값을 갖게 되는 정점의 인덱스 저장
            }

        check[vnear] = true; //최솟값을 갖게 되는 정점 선택 -> true

        for (int i = 1; i <= N; i++) {
            //아직 선택되지 않은 정점들에 대해 length[i] 갱신
            if (check[i] == false && length[i] > length[vnear] + weight[vnear][i]) {
                length[i] = length[vnear] + weight[vnear][i];
            }
        }
    }
}

int main() {
    //N개의 도시 수, M개의 버스 수 입력 받기
    scanf("%d %d", &N, &M);

    //가중치 그래프 초기화하기
    for (int i = 1; i <= N; i++) {
        for (int j = 1; j <= N; j++) {
            if (i == j) weight[i][j] = 0;	//출발지 = 도착지일때 비용 0
            else weight[i][j] = INF;	//모든 정점들 다 떨어져 있다고 가정(비용 최대)
        }
    }

    //버스의 출발지, 도착지에 해당하는 비용 입력받기
    while (M--) {
        int from, to, fee;
        scanf("%d %d %d", &from, &to, &fee);
        if (weight[from][to] > fee)
            weight[from][to] = fee;
    }

    //최소 비용을 구하려는 출발 도시와 도착 도시 입력 받기
    scanf("%d %d", &start, &dest);

    //다익스트라 알고리즘 통해 최소 비용 구하기
    dijkstra();

    //start-> dest의 최소 비용 출력
    printf("%d\n", length[dest]);

    return 0;
}