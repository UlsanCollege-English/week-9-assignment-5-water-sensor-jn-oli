import heapq

def streaming_median(nums):
    if not nums:
        return []
    
    lowers = []   # max-heap (store negatives)
    highers = []  # min-heap
    medians = []
    
    for num in nums:
        # Step 1: add number to one of the heaps
        if not lowers or num <= -lowers[0]:
            heapq.heappush(lowers, -num)
        else:
            heapq.heappush(highers, num)
        
        # Step 2: balance heaps
        if len(lowers) > len(highers) + 1:
            heapq.heappush(highers, -heapq.heappop(lowers))
        elif len(highers) > len(lowers):
            heapq.heappush(lowers, -heapq.heappop(highers))
        
        # Step 3: compute median
        if len(lowers) == len(highers):
            median = (-lowers[0] + highers[0]) / 2.0
        else:
            median = float(-lowers[0]) if isinstance(num, float) else -lowers[0]
        
        medians.append(median)
    
    return medians
