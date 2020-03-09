from parade.command import ParadeCommand


def check(tasks):
    nondeps_tasks = {}
    duplicate_tasks = {}
    circular_tasks = {}
    for task, deps in tasks.items():
        for dp in deps:
            # check for invalid dependencies
            if dp not in tasks:
                if task not in nondeps_tasks:
                    nondeps_tasks[task] = set()
                nondeps_tasks[task].add(dp)
            # check for duplicate dependencies
            # print(dp, deps)
            if deps.count(dp) > 1:
                if task not in duplicate_tasks:
                    duplicate_tasks[task] = set()
                duplicate_tasks[task].add((dp, deps.count(dp)))
            # check for circular dependence
            if dp == task:
                if task not in circular_tasks:
                    circular_tasks[task] = list()
                circular_tasks[task].append(dp)
            if dp != task and dp in tasks and task in tasks[dp]:
                if task not in circular_tasks:
                    circular_tasks[task] = list()
                circular_tasks[task].append({dp: tasks[dp]})

    nondeps_tasks = {k: list(v) for k, v in nondeps_tasks.items()}
    duplicate_tasks = {k: list(v) for k, v in duplicate_tasks.items()}
    # circular_tasks = {k: list(v) for k, v in circular_tasks.items()}
    return nondeps_tasks, duplicate_tasks, circular_tasks


class CheckCommand(ParadeCommand):
    requires_workspace = True

    def run_internal(self, context, **kwargs):
        flow_name = kwargs.get('flow-name')

        if flow_name:
            flowstore = context.get_flowstore()
            flow = flowstore.load(flow_name)
            if flow:
                deps = {k: list(v) for k, v in flow.deps.items()}  # 依赖
                for task in flow.tasks:
                    if task not in deps:
                        deps[task] = []
        else:
            deps = dict([(task.name, list(task.deps)) for task in context.load_tasks().values()])

        nondeps, duplicate, circular = check(deps)

        print('------------------------------------------')
        if len(nondeps) == 0 and len(duplicate) == 0 and len(circular) == 0:
            print('PASS')

        if len(nondeps) > 0:
            print('[Invalid Dependencies]')
            for k, v in nondeps.items():
                print(k, ' ==>  ', v)
            print('------------------------------------------')

        if len(duplicate) > 0:
            print('[Duplicate Dependencies]')
            for k, v in duplicate.items():
                print(k, ' ==>  ', v)
            print('------------------------------------------')

        if len(circular) > 0:
            print('[Circular Dependencies]')
            for k, v in circular.items():
                print(k, ' ==>  ', v)
            print('------------------------------------------')

    def config_parser(self, parser):
        parser.add_argument('flow-name', nargs='?', help='the flow to check')

    def short_desc(self):
        return 'check parade flow'
