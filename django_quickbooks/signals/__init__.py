from django.dispatch import Signal

qbd_task_create = Signal(providing_args=[
    "qb_operation",
    "qb_resource",
    "object_id",
    "content_type",
    "realm_id",
    "instance",
])

customer_created = Signal(providing_args=["qbd_model_mixin_obj", "realm_id"])
customer_updated = Signal(providing_args=["qbd_model_mixin_obj", "realm_id"])
invoice_created = Signal(providing_args=["qbd_model_mixin_obj", "realm_id"])
invoice_updated = Signal(providing_args=["qbd_model_mixin_obj", "realm_id"])

qb_object_created = Signal(providing_args=["instance", "realm"])
qb_object_updated = Signal(providing_args=["instance", "realm"])
qb_object_queried = Signal(providing_args=["instance", "realm"])
realm_authenticated = Signal(providing_args=["realm"])
qbd_first_time_connected = Signal(providing_args=["realm_id"])

from django_quickbooks.signals.customer import *
from django_quickbooks.signals.invoice import *
from django_quickbooks.signals.qbd_task import *
