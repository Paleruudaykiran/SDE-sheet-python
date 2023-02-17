class MaxHeap:
    def __init__(self,capacity):
        self.capacity = capacity
        self.size = 0
        self.array = [float('-inf')]*capacity 
    def push(self,data) :
        if self.size == self.capacity :
            return 'heap is full'
        else :
            self.array[self.size] = data
            index = self.size
            #hepify up
            while True :
                parentIndex = (index-1)//2
                if parentIndex < 0 :
                    break 
                else :
                    if self.array[parentIndex] < self.array[index] :
                        #swap
                        tp = self.array[parentIndex] 
                        self.array[parentIndex] = self.array[index]
                        self.array[index] = tp
                    else :
                        break
                    index = parentIndex
            self.size += 1
    def pop(self) :
        if self.size == 0 :
            print('heap is empty') 
            return -1
        data = self.array[0] 
        self.array[0] = self.array[self.size-1] 
        self.array[self.size-1] = float('-inf')
        index = 0
        #heapify down
        while True :
            leftChildIndex = 2*index + 1
            rightChildIndex = 2*index + 2
            if leftChildIndex >= self.capacity or rightChildIndex >= self.capacity:
                break
            largest = index 
            if self.array[leftChildIndex] > self.array[rightChildIndex] :
                largest = leftChildIndex
            else :
                largest = rightChildIndex
            
            if self.array[largest] > self.array[index]:
                tp = self.array[largest]
                self.array[largest] = self.array[index]
                self.array[index] = tp 
            else :
                break
            index = largest
        self.size -= 1
        return data

def kthSmallLarge(arr, n, k):
    heap = MaxHeap(n) 
    for x in arr :
        heap.push(x) 
    ans = [-1,-1]
    for i in range(n) :
        data = heap.pop() 
        #print(i,data,heap.array)
        if i == k-1 :
            ans[1] = data
        if i == n-k :
            ans[0] = data
    #print(ans)
    return ans