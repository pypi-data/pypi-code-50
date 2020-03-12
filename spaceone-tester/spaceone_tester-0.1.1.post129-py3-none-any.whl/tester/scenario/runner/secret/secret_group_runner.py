from spaceone.tester.scenario.runner.runner import ServiceRunner, print_json

__all__ = ['SecretGroupRunner']


class SecretGroupRunner(ServiceRunner):

    def __init__(self, clients, update_mode=False, credential_name2id={}):
        self.set_clients(clients)
        self.update_mode = update_mode
        self.credential_name2id = credential_name2id
        self.credential_group_name2id = {}

    def create_or_update_secret_group(self, secret_group, domain):
        for name, secret_name_list in secret_group.items():
            if self.update_mode:
                sg_obj = self._find_secret_group(name, domain)
                if sg_obj:
                    # secret is not mutable. It's only allow delete and create.
                    self._delete_secret_group(sg_obj)
            self._create_secret_group(name, secret_name_list, domain)
        return self.credential_group_name2id

    def _delete_secret_group(self, sg_obj):
        param = {
            'domain_id': sg_obj.domain_id,
            'credential_group_id': sg_obj.credential_group_id
        }
        self.secret.CredentialGroup.delete(param, metadata=self.get_meta())
        print("########### Secret Group DELETED ###############")

    def _find_secret_group(self, name, domain):
        param = {
            'name': name,
            'domain_id': domain.domain_id
        }
        results = self.secret.CredentialGroup.list(param, metadata=self.get_meta())

        if len(results.results) >= 1:
            print(f'Found {len(results.results)} secret(s).')
            return results.results[0]
        return None

    def _create_secret_group(self, name, secret_name_list, domain):
        default_param = {
            'name': name,
            'domain_id': domain.domain_id
        }
        sec_id_list = []
        for name in secret_name_list:
            sec_id = self.credential_name2id[name]
            sec_id_list.append(sec_id)
        default_param.update({'credentials': sec_id_list})

        credential_group_obj = self.secret.CredentialGroup.create(default_param, metadata=self.get_meta())
        self.credential_group_name2id[credential_group_obj.name] = credential_group_obj.credential_group_id
        self.append_terminator(
            self.secret.CredentialGroup.delete,
            {
                'domain_id': domain.domain_id,
                'credential_id': credential_group_obj.credential_group_id
            }
        )
        print("########### Create SECRET GROUP ###############")
        print_json(credential_group_obj)
