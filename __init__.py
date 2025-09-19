def simple_calculator(a,b,op):
   
    if op=="+":
        return a+b
    if op=="-":
        return a-b
    if op=="*":
        return a*b
    if op=="/":
        if b==0:
            return "Not defined"
        return a/b
    if op=="%":
        if b==0:
            return "Not defined"
        return a%b
    if op=="//":
        if b==0:
            return "Not defined"
        return a//b
    if op=="**":
        return a**b
        
a,op,b=input().split()
a=float(a)
b=float(b)
print(a, op, b ,"=" ,simple_calculator(a,b,op))