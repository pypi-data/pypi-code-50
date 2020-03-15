from timeit import default_timer as timer
from .mlnods import Mlnods
from .helpers import _globals, log
from . import __version__


def main(namespace, args):
    ts = Mlnods(**vars(namespace))
    log(f'\n --- mlnods {__version__} ---\n', prefix='')
        
    log('reading id file ...', wait=True)
    timer_start = timer()
    ts.parse_node_file()
    log(' [ok]', append=True, suffix=f' {(timer() - timer_start):.3f} seconds')
    
    if ts.format in ['blast', 'hssp']:
        if ts.format == 'blast':
            log(f'parsing {ts.format} output ... ', wait=True)
        elif ts.format == 'hssp':
            log(f'computing hssp scores ... ', wait=True)
        timer_start = timer()
        ts.parse_table_file()
        log(' [ok]', append=True, suffix=f' {(timer() - timer_start):.3f} seconds')
    
    log(f'building graph ...', wait=True)
    timer_start = timer()
    ts.parse_edge_file()
    log(' [ok]', append=True, suffix=f' {(timer() - timer_start):.3f} seconds')
    
    ts.get_stats()
    if ts.splits > ts.total:
        log(f' => Error. You want more sets ({ts.splits}) than there are IDs ({ts.total})')
        sys.exit(1)
    log(f'largest cluster size should be no more\n     than {ts.limit} to split {ts.total} IDs into {ts.splits} sets', prefix=' ==> ')
    log(f'IDs: {ts.total}', prefix=' ==> ')
    log(f'links: {len(ts.links)}', prefix=' ==> ')

    log(f'running analysis ... (this might take a while)', wait=True)
    timer_start = timer()
    ts.process()
    log(f' [ok] ', suffix=f'{(timer() - timer_start):.3f} seconds', append=True)

    log(f'total remaining            : {ts.sum_}', prefix=' ==> ')
    log(f'total deleted in splitting : {ts.del_}', prefix=' ==> ')
    link_del = ts.total_raw  - ts.sum_ - ts.del_
    if link_del:
        log(f'the rest ({link_del}) was deleted by links limitations.\n     if more instances are needed, loosen this feature', prefix=' ==> ')
    log(f'unique {ts.splits} instance sets found:', prefix=' ==> ')
    log(f'looking for approximately {ts.get_limit_muts()} per set', prefix=' ==> ')

    timer_start = timer()
    log(f'post-prossing ... ', wait=True)
    ts.post_process()
    log(f' [ok] ', suffix=f'{(timer() - timer_start):.3f} seconds', append=True)
    
    log(f'total clusters count : {ts.cluster_count}', prefix=' ==> ')
    log(f'largest cluster size : {ts.max} [#{ts.max_number}]', prefix=' ==> ')
    
    log(f'writing output files ... ', wait=True)
    timer_start = timer()
    ts.save_output()
    log(f' [ok] ', suffix=f'{(timer() - timer_start):.3f} seconds', append=True)
    log(f'unique sets of instances  : jctMuts[1..{ts.splits}]', prefix='   - ')
    log(f'list of clusters created  : {ts.out_jacked.name}', prefix='   - ')
    log(f'list of deleted instances : {ts.out_deleted.name}', prefix='   - ')
    log(f'saved to: {ts.outfolder.absolute()}', prefix=' ==> ')
