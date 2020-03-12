from spaceone.tester.scenario.runner.runner import ServiceRunner, print_json

__all__ = ['SecretRunner']


class SecretRunner(ServiceRunner):

    def __init__(self, clients, update_mode=False, region_name2id={}, zone_name2id={}, pool_name2id={}, project_name2id={}):
        self.set_clients(clients)
        self.update_mode = update_mode
        self.region_name2id = region_name2id
        self.zone_name2id = zone_name2id
        self.pool_name2id = pool_name2id
        self.project_name2id = project_name2id
        self.credential_name2id = {}

    def create_or_update_secrets(self, secrets, domain):
        for secret in secrets:
            if self.update_mode:
                secret_obj = self._find_secret(secret, domain)
                if secret_obj:
                    # secret is not mutable. It's only allow delete and create.
                    self._delete_secret(secret_obj)
            self._create_secret(secret, domain)
        return self.credential_name2id

    def _delete_secret(self, secret_obj):
        param = {
            'domain_id': secret_obj.domain_id,
            'credential_id': secret_obj.credential_id
        }
        self.secret.Credential.delete(param, metadata=self.get_meta())
        print("########### Secret DELETED ###############")

    def _find_secret(self, secret, domain):
        param = {
            'name': secret['name'],
            'domain_id': domain.domain_id
        }
        results = self.secret.Credential.list(param, metadata=self.get_meta())

        if len(results.results) >= 1:
            print(f'Found {len(results.results)} secret(s).')
            return results.results[0]
        return None

    def _create_secret(self, secret, domain):
        data = secret['data']
        region_name = secret['region_name']
        zone_name = secret['zone_name']
        region_id = self.region_name2id[region_name]
        zone_id = self.zone_name2id[region_name][zone_name]
        data['region_id'] = region_id
        data['zone_id'] = zone_id

        # Pool
        pool_name = secret.get('pool_name', None)
        if pool_name:
            pool_id = self.pool_name2id[pool_name]
            data['pool_id'] = pool_id

        # Project
        project_name = secret.get('project_name', None)
        if project_name:
            project_id = self.project_name2id[project_name]
            data['identity.project_id'] = project_id

        default_param = {
            'name': secret['name'],
            'data': data,
            'domain_id': domain.domain_id
        }
        credential_obj = self.secret.Credential.create(default_param, metadata=self.get_meta())
        self.credential_name2id[credential_obj.name] = credential_obj.credential_id
        self.append_terminator(
            self.secret.Credential.delete,
            {
                'domain_id': domain.domain_id,
                'credential_id': credential_obj.credential_id
            }
        )
        print("########### Create SECRET ###############")
        print_json(credential_obj)
        issue = self.secret.Credential.issue(
            {'credential_id': credential_obj.credential_id, 'domain_id': domain.domain_id},
            metadata=self.get_meta()
        )
        print("######### ISSUE SECRET #########")
        print_json(issue)
