BASE_URL = 'https://api.mailinator.com/v2'

DOMAINS_URL = f'{BASE_URL}/domains'
DOMAIN_URL = f'{DOMAINS_URL}/{{domain_id}}'

INBOXES_URL = f'{DOMAIN_URL}/inboxes'
INBOX_URL = f'{INBOXES_URL}/{{inbox_id}}'

MESSAGES_URL = f'{INBOX_URL}/messages'
MESSAGE_URL = f'{MESSAGES_URL}/{{message_id}}'

ATTACHMENTS_URL = f'{MESSAGE_URL}/attachments'
ATTACHMENT_URL = f'{ATTACHMENTS_URL}/{{attachment_id}}'
