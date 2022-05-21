import datetime as datetime_module
from rest_framework import serializers
from scoring.models import Receipt
from django.utils.timezone import utc


def get_time_diff(time_posted):
    now = datetime_module.datetime.utcnow().replace(tzinfo=utc)
    timediff = now - time_posted
    return timediff.total_seconds()


class ReceiptSerializer(serializers.ModelSerializer):
    class Meta:
        model = Receipt
        fields = '__all__'
        read_only_fields = ['score', 'datetime']
