//[���� 11401/C++] ���װ��3 

#include <iostream>
using namespace std;

//ū ���� -> 8 ����Ʈ ������(long long)���� ���� ����
//�丣���� �������� Ȱ���� A*B^(M-2)(mod M)���� B^(M-2)(mod M)���
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
	//�Է� �޴� ��(n, r), �������ִ� ��(p) �����ϴ� ���� ����
	long long n, r, p;

	cin >> n >> r; //�ڿ��� n, ���� r �ޱ�
	p = 1000000007LL; //�������ִ� ��

	long long ans = 1; //������ �� �����ϴ� ����
	long long t1 = 1; //�ӽð� ���� ����
	long long t2 = 1; //�ӽð� ���� ����

	for (long long i = 1; i <= n; i++) {
		t1 *= i; //n! ���
		t1 %= p; //n! ��� �� p �� �������� �� ������ ����
	}
	for (long long i = 1; i <= r; i++) {
		t2 *= i; //r! ���
		t2 %= p; //r! ��� �� p �� �������� �� ������ ����
	}
	for (long long i = 1; i <= n - r; i++) {
		t2 *= i; //r!(n-r)! ���
		t2 %= p; //r!(n-r)! ��� �� p �� �������� �� ������ ����
	}

	//B^(M-2) ���� t3 �� ����
	long long t3 = mul(t2, p - 2, p);
	t3 %= p; //B^(M-2)(modM)
	ans = t1 * t3; //A*B^(M-2)
	ans %= p; //A*B^(M-2)(mod M)
	cout << ans << '\n';
	return 0;
}