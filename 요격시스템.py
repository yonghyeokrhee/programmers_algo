def solution(targets):
    # line sweeping 문제로 풀자.
    target = sorted(targets, key = lambda  x: (x[0], x[1]))

    line = 0
    cnt = 0
    for t in target:
        if line < t[1] and line <= t[0]:
            line = t[1] #  line 뒤쪽으로 맞추기
            cnt += 1
        else:
            if t[0] < line: # line 앞쪽에서 시작하는 target들은 skip 한다.
                continue
    return cnt

print(solution([[4,5],[4,8],[10,14],[11,13],[5,12],[3,7],[1,4]]))