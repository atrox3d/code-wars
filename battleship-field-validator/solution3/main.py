from pathlib import Path
import logging

import helpers.load as load
import helpers.matrix as matrix
import helpers.logsetup as logsetup
import battleship


logsetup.setup(level='INFO')
logger = logging.getLogger(__name__)  # __name__ is a common choice

def main(solution):
    logger.info(f'START main: {logger.getEffectiveLevel() = }')
    extensions = 'json, ascii, csv'
    for file_path in load.get_files('battlefield.ascii'):
        tests = load.battlefield(file_path)
        for test in tests:
            name = test['name']
            battlefield = test['data']
            expected = test['expected']

            matrix.display(battlefield, clear_screen=False)
            result = solution(battlefield)
            logger.info(f'{name} -> {result = } -> {expected = }')
            
            print()
            print()


if __name__ == '__main__':
    import sys
    sys.exit(main(solution=battleship.validate_battlefield))