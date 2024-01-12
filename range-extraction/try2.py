def solution(data):
    result = []
    buffer = []
    prev = None
    for current in data:
        if prev is None:                    # first element, first loop
            buffer.append(current)          # stash it
        else:                               # all the other loops
            if current - prev == 1:         # do we have a sequence?
                buffer.append(current)      # stash it if yes
            else:                           # not in sequence
                if len(buffer) >= 3:        # do we have enough elements?
                    result.append(buffer)   # append sub list
                else:                       # not enough elements
                    result.extend(buffer)   # add elements as single
                    # result.append(current)  # * append current?
                result.append(current)
                buffer = []
        prev = current
    print(f'{result = }')
