from itertools import count

def fast_fib_generator():
    F = [1, 1]
    yield 1
    yield 1
    for k in count(1):
        F.append(F[k] ** 2 + F[k - 1] ** 2)
        yield F[-1]

        F.append(F[k] * (2 * F[k + 1] - F[k]))
        yield F[-1]

num = 0
blue_arr=[]
green_arr=[]
end_count = 300
for x in fast_fib_generator():
	num+=1
	print(num,x)
	
	if (num==end_count):
		break;
 