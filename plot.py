import matplotlib.pyplot as plt

with open('str.txt') as f:
	content = f.readlines()
content = [float(x.strip()[37::]) for x in content]


size=[]
scipy=[]
cvxpy=[]
j=0
k=1
for i in range(10,1000,20):
	size.append(i)
	scipy.append(content[j])
	cvxpy.append(content[k])
	j+=2
	k+=2

plt.plot(size,scipy,label='SciPy')
plt.plot(size,cvxpy,label='CVXPY')

plt.title('SciPy vs. CVXPY')
plt.xlabel('Size of square Matrix')
plt.ylabel('Time elapsed (s)')
plt.legend()

plt.show()