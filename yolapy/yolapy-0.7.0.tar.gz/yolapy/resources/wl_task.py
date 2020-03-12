class WLTaskResourceMixin(object):
    """Methods for managing WL Task resources."""

    def complete_wl_task(self, wl_task_id):
        """Complete WL Task.

        >>> yola.complete_wl_task('ae24b9c8048d4b0d9734263c7165bb79')
        {
            'id': 'ae24b9c8048d4b0d9734263c7165bb79,
            'status': 'completed,
            'details': {},
        }
        """
        return self.post('/wl-tasks/{}/complete/'.format(wl_task_id)).json()

    def fail_wl_task(self, wl_task_id, reason):
        """Fail WL Task.

        >>> yola.fail_wl_task(
        >>>    'ae24b9c8048d4b0d9734263c7165bb79', 'Unexpected Error'
        >>> )
        {
            'id': 'ae24b9c8048d4b0d9734263c7165bb79,
            'status': 'failed,
            'details': {'error': 'Unexpected Error'},
        }
        """
        return self.post(
            '/wl-tasks/{}/fail/'.format(wl_task_id),
            json={'reason': reason}
        ).json()
