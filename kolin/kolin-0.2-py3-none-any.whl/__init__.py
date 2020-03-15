def run():   
    import os
    kolin = input('file, ')
    

    fn = open(kolin, 'r')
    kn = fn.read()


    fn.close()
    os.system(kn)