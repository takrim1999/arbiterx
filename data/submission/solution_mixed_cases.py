def solve() -> None:
    n = int(input())
    if n & 1:
        print("YeS")
    else:
        print("NO")


if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        solve()
