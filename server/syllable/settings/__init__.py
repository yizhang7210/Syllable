import os

syllable_env = os.environ.get('SYLLABLE_ENV')

if syllable_env == 'PROD':
    from .production import *
elif syllable_env == 'DEPLOY':
    from .deploy import *
else:
    from .local import *
