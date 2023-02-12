#include <iostream>

int answer;

bool is_answer(long long curr,int A[], int N, int K)
{
    long long res = 0;
    for(int i = 0; i < N; i++)
    {
        res += A[i] / curr;
    }
    return res >= K;
}

void binary_search(int A[], int l, int r, int N, int K)
{
    int curr = l + (r - l) / 2;
    if(r < l) return;

    if (is_answer(curr,A,N,K))
    {
        if(curr > answer)
            answer = curr;
        binary_search(A,curr+1,r,N,K);
    }else{
        binary_search(A,l,curr-1,N,K);
    }
}

int main()
{
    answer = -1;
    int N,K;
    scanf("%d%d",&N,&K);
    int A[10000];
    
    int max_k = 0;
    for(int i = 0; i < N; i++)
    {
        scanf("%d", &A[i]);
        max_k = std::max(max_k,A[i]);
    }

    // binary search from 1 to MAX_K
    binary_search(A, 1, max_k+1,N,K);

    printf("%d\n", answer);

}
