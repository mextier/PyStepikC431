s = input()
n1,n2 = int(s.split()[0]),int(s.split()[1])
print('\n'.join(["FizzBuzz" if i%15==0 else "Fizz" if i%3==0 else "Buzz" if i%5==0 else str(i) for i in range(n1,n2+1)]))
