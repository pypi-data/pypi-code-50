import click

@click.group()
def ftimer():
    '''in barname vase ineke ma ye testi anajam bedi mke chi kara kardim o time haro dashte bashim'''


@ftimer.command()
def init():
    ''' create new workingtime.xls file as data base to store details'''
    current_path='milad'
    # successfull_msg=
#    f'Initialized empty Git repository in {current_path}'

    print('create new data base')
    pass 

@ftimer.command()
def state():
    '''show state of active work '''

@ftimer.command()
def start():
    '''insert start time of activity'''


@ftimer.command()
def stop():
    '''recode stop time of activity'''
    pass


@ftimer.command()
def log():
    pass

#
if __name__=='__main__':
    ftimer()