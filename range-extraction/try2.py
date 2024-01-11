def solution(data):
    result = []
    buffer = []
    prev = None
    for current in data:
        if prev is None:
            buffer.append(current)
        else:
            if current - prev == 1:
                buffer.append(current)
            else:
                if len(buffer) >= 3:
                    result.append(buffer)
                else:
                    result.extend(buffer)
                    result.append(current)
                result.append(current)
                buffer = []
        prev = current
    print(f'{result = }')
