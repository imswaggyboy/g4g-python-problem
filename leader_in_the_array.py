def leaders(self, A, N):
        l=[]

        max=A[N-1]

        l.append(A[N-1])

        for i in range(N-2,-1,-1):

            if A[i]>=max:

                l.append(A[i])

                max=A[i]

        l.reverse()

        return l



# leader = []
        # for i in range(N):
        #     vote = 0
        #     for j in range(i+1,N):
        #         if A[i]> A[j]:
        #             vote = vote+1
        #     if (len(A)-(i+1)) == vote:
        #         leader.append(A[i])
        # return leader
_______________________________________________________
        # n_l = [x for x in A]
        # leader = []
        # while len(A) >0:
        #     if A[0] ==max(A):
        #         leader.append(A[0])
        #         A.remove(A[0])
        #     else: A.remove(A[0])
        # return leader
