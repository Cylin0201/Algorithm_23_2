def insertion_sort(S):
    for i in range(1, len(S)):
        x = S[i]
        j = i - 1
        while (j >= 0 and x < S[j]):
            S[j + 1] = S[j]
            j -= 1
        S[j + 1] = x

def selection_sort(S):
    for i in range(len(S) - 1):
        smallest = i
        for j in range(i + 1, len(S)):
            if (S[j] < S[smallest]):
                smallest = j
        S[i], S[smallest] = S[smallest], S[i]

def exchange_sort(S):
    n = len(S)
    for i in range(n - 1):
        for j in range(i + 1, n):
            if (S[i] > S[j]):
                S[i], S[j] = S[j], S[i]

def bubble_sort(S):
    n = len(S)
    for i in range(n - 1):
        for j in range(n - 1 - i):
            if (S[j] > S[j + 1]):
                S[j], S[j + 1] = S[j + 1], S[j]

class List():
    def __init__(self, s):
        self.data = s[:]
        self.n = len(s)
    def insertion_sort(self):
        insertion_sort(self.data)
    def selection_sort(self):
        selection_sort(self.data)
    
S = [3, 2, 5, 7, 1, 9, 4, 6, 8]
bubble_sort(S)

print(S)
