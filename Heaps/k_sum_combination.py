import heapq

def kMaxSumCombination(a, b, n, k):
	# Sorting the arrays.
	a.sort()
	b.sort()
	
	# Using a max-heap.
	maxHeap = []
	heapq.heapify(maxHeap)
	maxHeap.append((-a[n-1] - b[n-1], n - 1, n - 1))
	
	# Using a set.
	mySet = set() 
	mySet.add((n - 1, n - 1))
	
	# Output array to store the K max sum combinations.
	result = []
	
	while(k > 0):
		# Remove the root of the max heap.
		sum, x, y = heapq.heappop(maxHeap)
		# sum, x, y = lst[0], lst[1], lst[2]
		
		# Add the sum to the output array.
		result.append(-sum)
		
		# Check if the indices (x-1, y) are present in the set.
		if((x - 1, y) not in mySet):
			maxHeap.append((-a[x - 1] - b[y], x - 1, y))
			mySet.add((x - 1, y))
		
		# Check if the indices (x, y-1) are present in the set.
		if((x, y - 1) not in mySet):
			maxHeap.append((-a[x] - b[y - 1], x, y - 1))
			mySet.add((x, y - 1))

		heapq.heapify(maxHeap)
		k -= 1
	
	# Return the output array.
	return result