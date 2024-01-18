import matrix as mx
def _bfs(maze, path=""):
    for x, pos in enumerate(maze[0]):
        print(f'{x, pos = }')
        if pos == 'O':
            start = x
            break
    else:
        raise ValueError('coulf not find "O" in the first row')


def main():
    matrix = mx.load()
    matrix = mx.convert_to_type(matrix, convert_type=int)
    matrix = mx.replace_items(matrix, {1: '#', 0: ' '})
    bordered_matrix = mx.format_border(matrix, ' ')
    mx.print_matrix(bordered_matrix)

if __name__ == '__main__':
    main()
