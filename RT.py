a = int(input('a:'))
b = int(input('b:'))
c = int(input('c:'))
if a*a+b*b == c*c or c*c+b*b == a*a or a*a+c*c == b*b:
    print(a, b, c, 'are right numbers')
