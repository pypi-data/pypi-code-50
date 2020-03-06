import unittest
import os
import sys
import coverage

def absolute_dir(dir: str):
    basedir = os.path.abspath(os.path.dirname(__file__))
    return os.path.join(basedir, dir)

cov = coverage.Coverage(source=['aws'])
cov.erase()
cov.start()

tests = unittest.TestLoader().discover('test')
result = unittest.TextTestRunner(verbosity=2).run(tests)
if result.wasSuccessful():
    cov.stop()
    cov.save()
    # cov.report()
    cov.html_report(directory='coverage/')
    sys.exit(0)

sys.exit(1)

