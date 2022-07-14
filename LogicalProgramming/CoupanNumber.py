import random
"""
N distinct Coupon Numbers, how many random numbers do you
need to generate distinct coupon number?
"""
def coupon(range_of_num):
	"""
	coupon numbers generator
	"""
	num = '0123456789'
	coupon_no = ''   # empty string
	for i in range(0, range_of_num):
		ran = random.randint(0, len(num) - 1)  # will generate 6 random numbers
		coupon_no += str(ran)   # append numbers in coupon_no
	return coupon_no

if __name__ == "__main__":
	print(coupon(6))