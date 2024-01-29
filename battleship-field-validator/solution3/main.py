import logging

import helpers.load as load
import helpers.matrix as matrix
import helpers.log.config as logconfig
import helpers.log.decorators as logdecorators
import battleship


config = logconfig.setup_logging(level='DEBUG')
logger = logging.getLogger(__name__)

logdecorators.decorate_module_functions(
                                module=battleship, 
                                decorator=logdecorators.logdecorator, 
                                log=logger.debug
            )

@logdecorators.logdecorator()
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