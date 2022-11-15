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
