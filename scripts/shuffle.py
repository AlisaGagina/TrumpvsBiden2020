import argparse
import csv
import random

def main():
	parser=argparse.ArgumentParser()
	parser.add_argument("input")
	parser.add_argument("output")

	args = parser.parse_args()
	with open(args.input) as f:
		l = []
		count = 0
		for line in f:
			print(count)
			if (count == 0):
				header = line
				count = count + 1
				continue
			
			print(line)
			l.append(line)
			
		
		random.shuffle(l)

	with open(args.output,"w") as out:
		out.write(header)
		for i in l:
			out.write(i)

if __name__ == '__main__':
	main()
