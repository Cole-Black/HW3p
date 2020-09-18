#Author: Cole Black-Stallard cdb5655@psu.edu
#Collaborator: NONE / SOLO
#Section: 012R

def digit_sum(n):
  if 0 <= n <= 9:
    return n 
  return (n % 10) + digit_sum(n // 10)

def run():
  nIN = int(input("Enter an int: "))
  print(f"sum of digits of {nIN} is {digit_sum(nIN)}.")

if __name__ == "__main__":
  run()