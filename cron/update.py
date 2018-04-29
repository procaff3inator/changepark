import sys
sys.path.append('../web')

from web import activity

pending_records = activity.get_pending_transactions()

for record in pending_records:
    print(record.status)
