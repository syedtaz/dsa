def main() -> None:
  a = 1
  b = 1
  k = 3

  while len(str(b)) < 1000:
    c = b + a
    a, b = b, c
    k += 1

  print(k - 1)

if __name__ == "__main__":
  main()