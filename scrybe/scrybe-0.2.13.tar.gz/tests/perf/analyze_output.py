import os
import pstats

filename = 'perf_test_titanic.out'
file_path = os.path.join(os.path.expanduser('~/tmp/perf_profiles'), filename)
p = pstats.Stats(file_path)

p.sort_stats('tottime').print_stats(20)
p.sort_stats('cumtime').print_stats(30)


filename = 'perf_test_titanic_with_src.out'
file_path = os.path.join(os.path.expanduser('~/tmp/perf_profiles'), filename)
p = pstats.Stats(file_path)

p.sort_stats('tottime').print_stats(20)
p.sort_stats('cumtime').print_stats(30)

p.sort_stats('cumtime').print_stats('numpy_datasets')

p.sort_stats('cumtime').print_stats('capture_current_contex')
p.sort_stats('cumtime').print_stats('nodes.py')


filename = 'perf_test_titanic_tb_fix.out'
file_path = os.path.join(os.path.expanduser('~/tmp/perf_profiles'), filename)
p = pstats.Stats(file_path)
p.sort_stats('tottime').print_stats(20)
p.sort_stats('cumtime').print_stats(30)

p.print_stats("get_src_line")


filename = 'perf_test_titanic_tb_no_scrybe.out'
file_path = os.path.join(os.path.expanduser('~/tmp/perf_profiles'), filename)
p = pstats.Stats(file_path)
p.sort_stats('tottime').print_stats(20)


filename = 'perf_test_titanic_tb_limit.out'
file_path = os.path.join(os.path.expanduser('~/tmp/perf_profiles'), filename)
p = pstats.Stats(file_path)
p.sort_stats('tottime').print_stats(20)
p.sort_stats('cumtime').print_stats(30)
p.sort_stats('cumtime').print_stats('source_context.py')
p.sort_stats('cumtime').print_stats('traceback.py')

filename = 'perf_test_titanic_wo_inspect.out'
file_path = os.path.join(os.path.expanduser('~/tmp/perf_profiles'), filename)
p = pstats.Stats(file_path)
p.sort_stats('tottime').print_stats(20)
p.sort_stats('cumtime').print_stats(30)


filename = 'perf_test_titanic_wo_inspect_limit10.out'
file_path = os.path.join(os.path.expanduser('~/tmp/perf_profiles'), filename)
p = pstats.Stats(file_path)
p.sort_stats('tottime').print_stats(20)
p.sort_stats('cumtime').print_stats(30)


p.sort_stats('cumtime').print_stats('numpy_datasets')
p.sort_stats('cumtime').print_stats('tracking_graph')
p.sort_stats('tottime').print_stats('source_context.py')

filename = 'perf_test_titanic_src_optim_limit15.out'
file_path = os.path.join(os.path.expanduser('~/tmp/perf_profiles'), filename)
p = pstats.Stats(file_path)
p.sort_stats('tottime').print_stats(20)
p.sort_stats('cumtime').print_stats(30)
