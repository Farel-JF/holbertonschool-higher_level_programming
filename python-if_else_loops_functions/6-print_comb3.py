#!/usr/bin/python3
for i in range(90):
  for j in range(i + 1, 10):
    print(f"{i}{j}", end="")
    if i != 8 or j != 9:
        print(f",", end="")
    else:
        print(f"")