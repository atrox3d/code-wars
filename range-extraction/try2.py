def solution(data):
    def create_result(data):
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
                    buffer = []                 # empty buffer
                    buffer.append(current)      # as for the first element
            prev = current                      # save prev

        if len(buffer) >= 3:                    # do we have spare elements?
            result.append(buffer)
        else:
            result.extend(buffer)
        
        return result
    
    def format_result(result):
        format_list = []
        for current in result:
            if isinstance(current, list):
                format_list.append(
                    f'{current[0]}-{current[-1]}'
                )
            elif isinstance(current, int):
                format_list.append(str(current))
            else:
                t = type(current)
                raise TypeError(f'unknown type {t} for {current}')
        
        return ','.join(format_list)

    result = create_result(data)
    print(f'{result = }')
    format_list = format_result(result)
    print(f'{format_list = }')
    return format_list
