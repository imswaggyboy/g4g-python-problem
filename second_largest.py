def print2largest(self,arr, n):
		# code here
		arr.sort()
		mx = arr[-1]
        for i in range(1,len(arr)):
            if arr[i] > mx:
                mx = arr[i]
        s_h = int()
        for i in range(1,n+1):
            if arr[-i]<mx:
                
                s_h = arr[-i]
                break
            else: s_h = -1
        return s_h
