long long fnTinhGiaiThua(int n){
	long long gt = 1;
	for (int i=2; i<=n; i++){
			gt *= i;
		}
		return gt;
}

long fnTinhTongChan(int n){
	long sum = 0;
	for (int i=1; i<=n; i++){
		if (i%2==0){
			sum+=i;
		}
	}
	return sum;
}

long fnTinhTongLe(int n){
	long sum = 0;
	for (int i=1; i<=n; i++){
		if (i%2!=0){
			sum+=i;
		}
	}
	return sum;
}

long long fnTinhLuyThua(int x, int n){
	long long kq = x;
	for (int i=2; i<=n; i++){
		kq *= x;
	}
	return kq;
}