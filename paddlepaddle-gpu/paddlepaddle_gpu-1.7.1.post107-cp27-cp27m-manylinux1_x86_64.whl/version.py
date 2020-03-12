# THIS FILE IS GENERATED FROM PADDLEPADDLE SETUP.PY
#
full_version    = '1.7.1'
major           = '1'
minor           = '7'
patch           = '1'
rc              = '0'
istaged         = False
commit          = '2a792de7c263fa038ba3e29285e4d9d7e86ab6ca'
with_mkl        = 'ON'

def show():
    if istaged:
        print('full_version:', full_version)
        print('major:', major)
        print('minor:', minor)
        print('patch:', patch)
        print('rc:', rc)
    else:
        print('commit:', commit)

def mkl():
    return with_mkl
