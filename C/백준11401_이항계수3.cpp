//[백준 11401/C++] 이항계수3 

#include <iostream>
using namespace std;

//큰 숫자 -> 8 바이트 정수형(long long)으로 변수 선언
//페르마의 소정리를 활용한 A*B^(M-2)(mod M)에서 B^(M-2)(mod M)계산
long long mul(long long x, long long y, long long p) {
	long long ans = 1;
	while (y > 0) {
		if (y % 2 != 0) {
			ans *= x;
			ans %= p;
		}
		x *= x;
		x %= p;
		y /= 2;
	}
	return ans;
}

int main() {
	//입력 받는 값(n, r), 나누어주는 값(p) 저장하는 변수 생성
	long long n, r, p;

	cin >> n >> r; //자연수 n, 정수 r 받기
	p = 1000000007LL; //나누어주는 수

	long long ans = 1; //나머지 값 저장하는 변수
	long long t1 = 1; //임시값 저장 변수
	long long t2 = 1; //임시값 저장 변수

	for (long long i = 1; i <= n; i++) {
		t1 *= i; //n! 계산
		t1 %= p; //n! 계산 후 p 로 나누었을 때 나머지 저장
	}
	for (long long i = 1; i <= r; i++) {
		t2 *= i; //r! 계산
		t2 %= p; //r! 계산 후 p 로 나누었을 때 나머지 저장
	}
	for (long long i = 1; i <= n - r; i++) {
		t2 *= i; //r!(n-r)! 계산
		t2 %= p; //r!(n-r)! 계산 후 p 로 나누었을 때 나머지 저장
	}

	//B^(M-2) 변수 t3 에 저장
	long long t3 = mul(t2, p - 2, p);
	t3 %= p; //B^(M-2)(modM)
	ans = t1 * t3; //A*B^(M-2)
	ans %= p; //A*B^(M-2)(mod M)
	cout << ans << '\n';
	return 0;
}