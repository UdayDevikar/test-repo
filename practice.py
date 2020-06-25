# a=[]
# s='qwdftr'
# n=2
# vowels= {'e', 'a', 'i', 'o', 'u'}
# a=[s[i:i+n] for i in range(len(s)) if len(s[i:i+n])==n]


# count=[]

# for i in a:
# 	sum=0
# 	for j in i:
# 		if j in vowels:
# 			sum+=1
# 	count.append(sum)

# num = count.index(max(count))
# if num==0 and len(set(count))==1:
# 	print('Not found!')
# else:
# 	print(a[num])	



other_cities = ["Strasbourg", "Freiburg", "Stuttgart", 
                "Vienna / Wien", "Hannover", "Berlin", 
                "Zurich"]

city_iterator = iter(other_cities)
while city_iterator:
	try:
	    city = next(city_iterator)
	    print(city)
	except StopIteration as e:
		break

