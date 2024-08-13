import sys
input=sys.stdin.readline
k,n =map(int,input().split())
array = []
for i in range(k):
	array.append(int(input()))
start=1
end=max(array)
while(start<=end):
	mid = (start+end)//2
	total = 0
	for i in array:
		total += i//mid
	if total >= n:
		start=mid+1
		result = mid
	else:
		end=mid-1
print(result)