import numpy as np
import random
import math

def get_data(correlated=True, count=1000, start=1, end=1000):
	arr = np.random.randint(start, end, count)
	if correlated:
		arr2 = [(i, i * 2) for i in arr]
	else:
		arr2 = [(i, random.randint(200, 300)) for i in arr]
		
	return arr2

def cumulative_entropy_hist(arr, bins=10):
	hist, bin_edges = np.histogram(arr, density=True, bins=bins)
	cum_distrib = np.cumsum(hist*np.diff(bin_edges))
	try:
		cum_entropy_args = [cd * math.log(cd * 1.0, 2) for cd in cum_distrib]
	except Exception as e:
		print(e)
		print(cum_distrib)
		raise

	return -sum(cum_entropy_args * np.diff(bin_edges))

def cumulative_entropy_arr(arr):
	bin_edges = sorted(set(arr))
	count = len(bin_edges)
	cum_distrib = np.cumsum(np.diff(bin_edges) * [1.0/count for i in xrange(count-1)])
	cum_entropy_args = [cd * math.log(cd * 1.0, 2) for cd in cum_distrib]
	return -sum(cum_entropy_args * np.diff(bin_edges))

def corr(data):
	yx = {}
	for x, y in data:
		yx.setdefault(y, [])
		yx[y].append(x)

	ys = sorted(yx.keys())
	hxy = sum([cumulative_entropy_arr(yx[y]) * (1.0/len(ys)) for y in ys])
	hx = cumulative_entropy_hist(np.array([i[0] for i in data]))
	return hx - hxy

if __name__ == "__main__":
	for start, end in [(1, 100), (10, 20), (1000, 10000)]:
		print("\nNot correlated")
		data = get_data(correlated=False, start=start, end=end)
		print("{0}-{1} {2}".format(start, end, corr(data)))

		print("Correlated")
		data = get_data(correlated=True, start=start, end=end)
		print("{0}-{1} {2}".format(start, end, corr(data)))
