def main():
  
    a, b, c = input().split()
    a = int(a)
    b = int(b)
    c = int(c)
    
    if a>b>c:
        print(c)
        print(b)
        print(a)
        print()
        print(a)
        print(b)
        print(c)

    if a>c>b:
        print(b)
        print(c)
        print(a)
        print()
        print(a)
        print(b)
        print(c)

    if b>c>a:
        print(a)
        print(c)
        print(b)
        print()
        print(a)
        print(b)
        print(c)

    if b>a>c:
        print(c)
        print(a)
        print(b)
        print()
        print(a)
        print(b)
        print(c)

    if c>a>b:
        print(b)
        print(a)
        print(c)
        print()
        print(a)
        print(b)
        print(c)

    if c>b>a:
        print(a)
        print(b)
        print(c)
        print()
        print(a)
        print(b)
        print(c)

        
main()
