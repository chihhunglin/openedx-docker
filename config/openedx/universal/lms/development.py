from ..devstack import *

# Load module store settings from config files
update_module_store_settings(MODULESTORE, doc_store_settings=DOC_STORE_CONFIG)

# Set uploaded media file path
MEDIA_ROOT = "/openedx/data/uploads/"

# Deactivate forums
FEATURES['ENABLE_DISCUSSION_SERVICE'] = False

# Deactivate syslog-based loggers which don't work inside docker containers
LOGGING['handlers'].pop('local')
LOGGING['handlers'].pop('tracking')
LOGGING['loggers'].pop('tracking')
LOGGING['loggers']['']['handlers'] = ['console']

# Create folders if necessary
import os
for folder in [LOG_DIR, MEDIA_ROOT, STATIC_ROOT_BASE]:
    if not os.path.exists(folder):
        os.makedirs(folder)
