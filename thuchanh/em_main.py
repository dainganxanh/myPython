with open('IN.IN') as fi:
	fi.readline()
	a = fi.readline()
ma = list(a.split(' '))

t = set(ma)
mb=list(t)
#thêm dòng sau nếu muốn sắp xếp
mb.sort()
''' tạo list không trùng bằng for
for a in ma:
	if a not in mb:
		mb.append(a) 
'''		
with open('OUT.OT','w') as fo:
	for i in mb:
		count = ma.count(i)
		fo.write(str(i) + ' ' + str(count) + '\n')	
	print('Đã ghi vào file OUT.OT')