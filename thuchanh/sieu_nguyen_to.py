def snt(a):
	if a > 0 and a <=3:
		return True
	t = int(a**0.5)
	for x in range(2,t+1):
		if a % x == 0:
			return False
			break
		else: return True

def sieunt(a):
	t = snt(a)
	while a != 0:
		if snt(a): 
			t = True
			a //= 10
		else: 
			t = False
			break
	return t

#n = int(input('Nhập số chữ số:'))
n = 5
t = '1'+'0'*(n-1)
n1 = int(t)
count = 0

for i in range(n1,n1*10):
	if sieunt(i):
		#print(i, end=' ')
		count += 1

print()
print(f'Tổng cộng có {count} số là siêu nguyên tố có {n} chữ số')
input()