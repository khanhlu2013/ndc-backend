# from event.models import Event,Event_rate
# from ndc_user.models import Ndc_user
# from django.conf import settings
# import datetime
# from event.models import Event_rate,Attendance,Default_rate,Venue
# from django.db import DataError

# def get_venue(venue_id):
#     return Venue.objects.get(pk=venue_id)

# def get_venue_lst():
#     return Venue.objects.all()

# def get_event(event_id):
#     return Event.objects.get(pk=event_id)

# def get_event_lst():
#     return Event.objects.all()

# def get_event_default_rate_lst():
#     """
#         Exception is raised if admin have not define all default rate
#     """
#     result_lst = []
#     default_rate_lst = Default_rate.objects.all()
#     for rate_type in [item[0] for item in Event_rate.DANCE_RATE_LST]:
#         if rate_type not in [item.rate_type for item in default_rate_lst]
#             raise Exception()

#     return default_rate_lst

# def create_event(venue_id,date,weekly):
#     event_lst = []
#     default_rate_lst = get_event_default_rate_lst()
#     for i in range(weekly):
#         event = Event.objects.create(
#             date = date + datetime.timedelta(days=i*7),
#             venue_id = venue_id
#         )
#         for default_rate in [item for item in default_rate_lst]:
#             event_rate = Event_rate.objects.create(
#                 event = event,
#                 rate_type = default_rate.rate_type,
#                 rate_amount = default_rate.rate_amount
#             )

#         event_lst.append(event)
#     return event_lst

# def insert_or_edit_event_default_rate(rate,amount):
#     obj,created = Default_rate.objects.update_or_create(defaults={'rate_amount':amount},rate=rate)
#     return obj

# def insert_attendance(event_id,user_id,anonymous_first_name,anonymous_last_name,event_rate_id,payment_type):
#     event_rate = Event_rate.objects.get(pk=event_rate_id)
#     if event_rate.event.id != event_id:
#         raise DataError

#     return Attendance.objects.create(
#         event_id = event_id,
#         user_id = user_id,
#         anonymous_first_name = anonymous_first_name,
#         anonymous_last_name = anonymous_last_name,
#         event_rate_id = event_rate_id,
#         payment_type = payment_type
#     )