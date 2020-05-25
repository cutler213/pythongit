a=5
b=0

try:
    print(a/b)

except Exception as e:
    print("u can't divide by 0 ",e)

finally:
    print("bye")