from spaceone.tester.scenario.runner.runner import ServiceRunner, print_json

__all__ = ['CollectorRunner']


class CollectorRunner(ServiceRunner):

    def __init__(self, clients, update_mode=False, credential_name2id={}, credential_group_name2id={}):
        self.set_clients(clients)
        self.update_mode = update_mode
        self.credential_name2id = credential_name2id
        self.credential_group_name2id = credential_group_name2id
        self.regist_collectors = []

    def create_or_update_collectors(self, collectors, domain):
        for collector in collectors:
            collector_obj = None
            if self.update_mode:
                collector_obj = self._find_collector(collector, domain)
                if collector_obj:
                    collector_obj = self._update_collector(collector, collector_obj)

            if collector_obj is None:
                self._create_collector(collector, domain)
        return self.regist_collectors

    def collect(self, domain):
        for collect in self.regist_collectors:
            collector_id = collect.collector_id
            params2 = {
                'collector_id': collector_id,
                'collect_mode': 'ALL',
                'domain_id': domain.domain_id
            }
            job = self.inventory.Collector.collect(params2, metadata=self.get_meta())
            print("########### Do Collect!! ###############")
            print_json(job)

    def _update_collector(self, collector, collector_obj):
        plugin_info = collector['plugin_info']
        if 'credential' in plugin_info:
            plugin_info['credential_id'] = self.credential_name2id[plugin_info['credential']]
            del plugin_info['credential']
        if 'credential_group' in plugin_info:
            plugin_info['credential_group_id'] = self.credential_group_name2id[plugin_info['credential_group']]
            del plugin_info['credential_group']

        params = {
            'name': collector['name'],
            'plugin_info': plugin_info,
            'priority': collector.get('priority', 1),
            'domain_id': collector_obj.domain_id,
            'collector_id': collector_obj.collector_id,
            'tags': collector.get('tags', {})
        }
        collector_obj = self.inventory.Collector.update(params, metadata=self.get_meta())
        print("########### Update Collector ###############")
        print_json(collector_obj)
        self.regist_collectors.append(collector_obj)
        return collector_obj

    def _find_collector(self, collector, domain):
        name = collector['name']
        param = {
            'name': name,
            'domain_id': domain.domain_id
        }
        results = self.inventory.Collector.list(param, metadata=self.get_meta())
        if len(results.results) >= 1:
            print(f'Found {len(results.results)} "{name}" collectors.')
            return results.results[0]
        return None

    def _create_collector(self, collector, domain):
        plugin_info = collector['plugin_info']
        # Credential
        credential = plugin_info.get('credential', None)
        if credential:
            plugin_info['credential_id'] = self.credential_name2id[credential]
            del plugin_info['credential']
        # Credential Group
        credential_group = plugin_info.get('credential_group', None)
        if credential_group:
            plugin_info['credential_group_id'] = self.credential_group_name2id[credential_group]
            del plugin_info['credential_group']

        params = {
            'name': collector['name'],
            'plugin_info': plugin_info,
            'priority': collector.get('priority', 1),
            'domain_id': domain.domain_id,
            'tags': collector.get('tags', {})
        }
        print("#### TEST ####")
        print(params)
        print("#### TEST2 ####")
        print(self.get_meta())
        print("### XXXXX ####")
        collector_obj = self.inventory.Collector.create(params, metadata=self.get_meta())
        print("########### Create Collector ###############")
        print_json(collector_obj)
        self.regist_collectors.append(collector_obj)
        self.append_terminator(
            self.inventory.Collector.delete,
            {
                'domain_id': domain.domain_id,
                'collector_id': collector_obj.collector_id
            }
        )
