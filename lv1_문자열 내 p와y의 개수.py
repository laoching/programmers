def solution(senten):
    senten = senten.lower()
    p_cnt = 0
    y_cnt = 0
    for i in senten:
        if i == 'p':
            p_cnt += 1
        elif i == 'y':
            y_cnt += 1

    if p_cnt == y_cnt:
        return True
    else:
        return False
