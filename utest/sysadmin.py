answer = -1

def is_answer(curr, A, N, K):
    res = 0
    for i in range(N):
        res += A[i] // curr
    return res >= K

def binary_search(A, l, r, N, K):
    global answer
    curr = l + (r - l) // 2
    if r < l:
        return

    if is_answer(curr, A, N, K):
        if curr > answer:
            answer = curr
        binary_search(A, curr+1, r, N, K)
    else:
        binary_search(A, l, curr-1, N, K)

answer = -1
N, K = map(int, input().split())
A = list(map(int, input().split()))
max_k = max(A)

binary_search(A, 1, max_k+1, N, K)

print(answer)
