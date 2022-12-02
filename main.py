from functools import reduce

def parse_input():
  with open('full_input.txt') as f:
    lines = f.read().split('\n\n')
    for i, line in enumerate(lines):
      lines[i] = line.split()
    
    return lines

def getSubArraySum(array):
  return reduce(lambda sum, item: sum + int(item), array, 0)

def solutionOne(input):
  return max(input)

def solutionTwo(input):
  return sum(list(sorted(input, reverse=True))[0:3])

def main():
  input = list(map(getSubArraySum, parse_input()))
  print("1:", solutionOne(input))
  print("2:", solutionTwo(input))

if __name__ == "__main__":
    main()