if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    max_score = max(arr)
    sec = -100
    for score in arr:
        if score > sec and score < max_score:
            sec=score
    print(sec)