import datetime as datetime_module
import math
from celery import shared_task
from django.utils.timezone import utc
from scoring.models import Receipt


def get_time_diff(time_posted):
    now = datetime_module.datetime.utcnow().replace(tzinfo=utc)
    timediff = now - time_posted
    return timediff.total_seconds()


@shared_task
def async_create(validated_data):
    distance = validated_data.get('distance')
    user_id = validated_data.get('user_id')
    if not distance and not user_id:
        return
    count_of_this_month_receipts = 0
    sum_of_this_month_distances = 0
    for receipt in Receipt.objects.all():
        if get_time_diff(receipt.datetime) < 30 * 24 * 60 * 60:
            count_of_this_month_receipts += 1
            sum_of_this_month_distances += receipt.distance
    if count_of_this_month_receipts == 0:
        score = math.floor(distance ** 2) + 1
    else:
        score = math.floor((distance / (sum_of_this_month_distances / count_of_this_month_receipts)) ** 2) + 1
    datetime = datetime_module.datetime.utcnow().replace(tzinfo=utc)

    receipt = Receipt.objects.create(distance=distance, user_id=user_id, score=score, datetime=datetime)
    receipt.save()
