def add(x,y):
	return (x+y)

def sub(x,y):
	return x-y

def mul(x,y):
	return x*y

def div(x,y):
	return x/y

n1=int(input("Give the first no:"))
n2=int(input("give the second no :"))

l={1:'add',2:'subtract',3:'multiply',4:'divide'}
print(l)
x=int(input("Select one option : "))

if x==1:
	print("result = ",add(n1,n2))
elif x==2:
	print("result = ",sub(n1,n2))
elif x==3:
	print("result = ",mul(n1,n2))
elif x==4:
	print("result = ",div(n1,n2))
else:
	print("invalid option")

