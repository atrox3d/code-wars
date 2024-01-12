def solution(data):
    def create_result(data):
        '''
        scans data list, looking for ranges
        every range found is saved as a sublist
        '''
        result = []                             # will contain result list
        buffer = []                             # accumulator buffer for ranges
        prev = None                             # previous element, None when loop starts
        for current in sorted(data):
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
            result.append(buffer)               # append sublist
        else:
            result.extend(buffer)               # add elements as single
        
        return result
    
    def format_result(result):
        '''
        formats the result as a comma-separated string
        - integers to strings
        - list to ranges (n-nx)
        '''
        format_list = []
        for current in result:
            if isinstance(current, list):
                format_list.append(f'{current[0]}-{current[-1]}')
            elif isinstance(current, int):
                format_list.append(str(current))
            else:
                raise TypeError(f'unknown type {type(current)} for {current}')
        
        return ','.join(format_list)

    result = create_result(data)
    # print(f'{result = }')
    format_list = format_result(result)
    # print(f'{format_list = }')
    return format_list
