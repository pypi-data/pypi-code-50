# -*- coding: utf-8 -*-
"""Leankit Client class file."""

import logging
import sys


class Client(object):
    """Leankit Client class."""

    def __init__(self, auth, leankit):
        """Initialize a class instance."""
        self.auth = auth
        self.leankit = leankit
        self.verbose = leankit.verbose

        self.exceptions = [
            'bitsdb@broadinstitute.org',
        ]

    def _add_users(self, add):
        """Add users to Leankit."""
        added = []
        for google_user in add:
            user = self.leankit.prepare_user(
                first_name=google_user['name']['givenName'],
                last_name=google_user['name']['familyName'],
                email=google_user['primaryEmail'],
                external_id=google_user['id'],
            )
            if 'id' in self.leankit.create_user(user):
                username = user['userName']
                added.append(username)
                print('  + Added user: {}'.format(username))
            else:
                error = 'Failed to add user: {}'.format(google_user['primaryEmail'])
                logging.error(error)
        return added

    def _delete_users(self, delete):
        """Disable users in Leankit."""
        disabled = []
        for user in delete:
            user_id = user['id']
            # disable instead of deleting
            if self.leankit.disable_user(user_id):
                username = user['userName']
                disabled.append(username)
                print('  - Disabled user: {}'.format(username))
            else:
                error = 'Failed to disable user: {}'.format(user['userName'])
                logging.error(error)
        return disabled

    def _get_leankit_group_user_ids(self, google):
        """Return a dict of Google user ids from lean kit group."""
        # get leankit google group members
        group = 'leankit-users@broadinstitute.org'
        if self.verbose:
            print('Getting Users from {}...'.format(group))

        user_ids = {}
        for member in google.directory().get_derived_members(group):
            uid = member['id']
            user_ids[uid] = member
        return user_ids

    def _get_google_emails(self, google, user_ids):
        """Return a dict of google users by email."""
        google_emails = {}
        for uid in user_ids:
            try:
                user = google.directory().get_user(uid)
                email = user['primaryEmail']
                if not user['suspended']:
                    google_emails[email] = user
                else:
                    print('Terminated user: {}'.format(email))
            except Exception:
                email = user_ids[uid]['email']
                print('Google User not found: {}'.format(email))
                # print(e)
                continue
        return google_emails

    def _get_users_to_add(self, current, new):
        """Return a list of users to add."""
        add = []
        for email in sorted(new):
            if email not in current:
                add.append(new[email])
        return add

    def _get_users_to_delete(self, current, new):
        """Return a list of users to delete."""
        delete = []
        for email in sorted(current):
            if email in self.exceptions:
                continue
            if email not in new:
                delete.append(current[email])
        return delete

    def _update_users(self, emails, google_emails):
        """Update a single user in Leankit."""
        # updating users
        for email in sorted(emails):
            if email not in google_emails:
                continue
            google_user = google_emails[email]

            old = emails[email]
            new = self.leankit.prepare_user(
                first_name=google_user['name']['givenName'],
                last_name=google_user['name']['familyName'],
                email=google_user['primaryEmail'],
                external_id=google_user['id'],
            )

            output = []
            for key in sorted(old):
                # ignore certain keys
                if key in [
                        'id',
                        'meta',
                ]:
                    new[key] = old[key]

                # don't overwrite administrator or boardCreator permissions
                if key == 'urn:scim:schemas:extension:leankit:user:1.0':
                    new[key]['administrator'] = old[key]['administrator']
                    new[key]['boardCreator'] = old[key]['boardCreator']
                    new[key]['lastAccess'] = old[key]['lastAccess']

                # compare old and new value
                old_value = old[key]
                new_value = new.get(key)
                if old_value != new_value:
                    output.append('   {}: {} -> {}'.format(
                        key,
                        old_value,
                        new_value,
                    ))

            if output:
                print('\nUpdating {}'.format(email))
                print('\n'.join(output))

                # don't update metadata or lastAccess time
                del new['meta']
                del new['urn:scim:schemas:extension:leankit:user:1.0']['lastAccess']

                # update the user
                response = self.leankit.update_user(new['id'], new)
                if 'id' in response:
                    print('   o Updated user: {}'.format(email))

    def users_list(self, searchfilter=None):
        """List users in Leankit."""
        if self.verbose:
            print('Getting users from Leankit...')
        users = self.leankit.get_users(searchfilter=searchfilter)
        print('Users: {}\n'.format(len(users)))

        key = 'urn:scim:schemas:extension:leankit:user:1.0'
        for user in sorted(users, key=lambda x: x['userName']):
            admin = ''
            if user[key]['administrator']:
                admin = ' (Admin)'
            print('{}: {} [{}]{}'.format(
                user['userName'],
                user['name']['formatted'],
                user['id'],
                admin
            ))

    def users_update(self):
        """Update users in Leankit."""
        # connect to google
        google = self.auth.google()
        google.auth_service_account(google.scopes, google.subject)

        # get leankit google user ids from google groups
        user_ids = self._get_leankit_group_user_ids(google)

        # sort google bits users by their google primaryEmail
        google_emails = self._get_google_emails(google, user_ids)

        # get leankit users
        users = self.leankit.get_users()
        print('Users: {}'.format(len(users)))

        # sort leankit users by email
        emails = {}
        for user in users:
            email = user['userName']
            emails[email] = user

        # add users
        add = self._get_users_to_add(emails, google_emails)
        if add:
            print('\nUsers to Add [{}]:'.format(len(add)))
            self._add_users(add)

        # delete users
        delete = self._get_users_to_delete(emails, google_emails)

        # make sure we don't delete too many users!!!
        if len(delete) > (len(users)/5):
            logging.error('Too many users to delete! [{}/{}]'.format(
                len(delete),
                len(users),
            ))
            sys.exit()

        if delete:
            print('\nUsers to Delete [{}]:'.format(len(delete)))
            self._delete_users(delete)

        # update users
        self._update_users(emails, google_emails)
