def solution(arr, k):

    result = []
    for i in arr:
        if k % 2 != 0: #홀수
            i *= k
            result.append(i)
        else:
            i += k
            result.append(i)
    
    return result