def solution(data):
    prev = diff = 0
    result = group = []
    for current in data:
        diff = current - prev
        if diff == 1:
            group.append(prev)
        else:
            group.append(prev)
            if len(group) >= 3:
                result.append(group)
            else:
                result.extend(group)
            group = []
        prev = current
    return result
