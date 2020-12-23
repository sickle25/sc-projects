"""
File: largest_digit.py
Name: Ray
----------------------------------
This file recursively prints the biggest digit in
5 different integers, 12345, 281, 6, -111, -9453
If your implementation is correct, you should see
5, 8, 6, 1, 9 on Console.
"""


def main():
	print(find_largest_digit(12345))      # 5
	print(find_largest_digit(281))        # 8
	print(find_largest_digit(6))          # 6
	print(find_largest_digit(-111))       # 1
	print(find_largest_digit(-9453))      # 9


def find_largest_digit(n):
	"""
	:param n:
	:return:
	"""
	if n <10 and n > -10:
		if n < 0:
			n = -n
		return n
	else:
		max = find_helper(n, 0)
		return max


def find_helper(n,max):

	if n < 0:
		n = -n

	if n == 0:
		return max

	else:
		a = int(n/10)

		if a<10 and n < 10:
			if n < 10 and n > max:
				max = n
			b=a

		else:
			b = n - (a*10)


		if max < b:
			max = b



		return find_helper(a,max)



if __name__ == '__main__':
	main()
