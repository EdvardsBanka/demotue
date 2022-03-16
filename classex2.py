print("Pick a number")
user = int(input())

def recursive(n):
    if n ==0:
        return 0
    else:
        print(n)
        return n + recursive(n - 1)
recursive(user)
