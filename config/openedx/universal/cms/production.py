import os
from ..aws import *

update_module_store_settings(MODULESTORE, doc_store_settings=DOC_STORE_CONFIG)

MEDIA_ROOT = "/openedx/data/uploads/"
FEATURES['ENABLE_DISCUSSION_SERVICE'] = False

# Deactivate syslog-based loggers which don't work inside docker containers
# TODO redirect tracking logs to files
LOGGING['handlers'].pop('local')
LOGGING['handlers'].pop('tracking')
LOGGING['loggers'].pop('tracking')
LOGGING['loggers']['']['handlers'] = ['console']

# Create folders if necessary
for folder in [LOG_DIR, MEDIA_ROOT, STATIC_ROOT_BASE]:
    if not os.path.exists(folder):
        os.makedirs(folder)

ALLOWED_HOSTS = [
    ENV_TOKENS.get('CMS_BASE'),
]

DEFAULT_FROM_EMAIL = 'registration@' + ENV_TOKENS['LMS_BASE']
DEFAULT_FEEDBACK_EMAIL = 'feedback@' + ENV_TOKENS['LMS_BASE']
SERVER_EMAIL = 'devops@' + ENV_TOKENS['LMS_BASE']
