def parse_input():
  with open('test_input.txt') as f:
    lines = f.read().split('\n\n')
    for i, line in enumerate(lines):
      lines[i] = line.split()
    
    return lines

def stringsToInts(array):
  out = []
  for s in array:
    out.append(int(s))
  return sum(out)

def main():
  input = parse_input()
  print(max(map(stringsToInts, input)))

if __name__ == "__main__":
    main()