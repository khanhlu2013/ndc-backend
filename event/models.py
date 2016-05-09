from django.db import models
from member.models import Member

class Venue(models.Model):
    name = models.CharField(max_length=100,unique=True)
    
    def __str__(self):
        return self.name

class Event(models.Model):
    date = models.DateField()
    venue = models.ForeignKey(Venue)
    
    class Meta:
        unique_together = ('date', 'venue',)

    def __str__(self):
        return str(self.venue) + ' ' + str(self.date)

class Event_rate(models.Model):
    """
        For past events to be self-contained, each event have to know about each own rate.
    """
    DANCE_ONLY_MEMBER = 0
    DANCE_AND_LESSON_MEMBER = 1
    DANCE_ONLY_NON_MEMBER = 2
    DANCE_AND_LESSON_NON_MEMBER = 3
    TIP_FOR_BLUES = 4
    UCSC = 5
    EXEMPT = 6
    DJ_INSTRUCTOR = 7
    VOLUNTEER = 8
    COMP = 9

    DANCE_RATE_LST = (
        (DANCE_ONLY_MEMBER,'Member dance only'),
        (DANCE_AND_LESSON_MEMBER,'Member lesson and dance'),
        (DANCE_ONLY_NON_MEMBER,'Non-member dance only'),
        (DANCE_AND_LESSON_NON_MEMBER,'Non-member lesson and dance'),
        (TIP_FOR_BLUES,'Tips for blues'),
        (UCSC,'UC Santa Cruz student'),
        (EXEMPT,'Exempt'),
        (DJ_INSTRUCTOR,'DJ / Instructor'),
        (VOLUNTEER,'Volunteer'),
        (COMP,'Comp')
    )

    event = models.ForeignKey(Event,related_name='event_rate_lst')
    rate_type = models.IntegerField(choices=DANCE_RATE_LST)
    rate_amount = models.DecimalField(max_digits=5, decimal_places=2)


class Attendance(models.Model):
    CASH = 0
    CREDIT = 1

    PAYMENT_TYPE_LST = (
        (CASH,'Cash'),
        (CREDIT,'Credit')
    )

    event = models.ForeignKey(Event,related_name='attendance_lst')
    member = models.ForeignKey(Member,blank=True,null=True)
    
    date_time = models.DateTimeField(auto_now_add=True)    
    anonymous_first_name = models.CharField(max_length=100,blank=True,null=True)
    anonymous_last_name = models.CharField(max_length=100,blank=True,null=True)
    rate_type = models.IntegerField(choices=Event_rate.DANCE_RATE_LST)
    rate_amount = models.DecimalField(max_digits=5, decimal_places=2)
    payment_type = models.IntegerField(choices=PAYMENT_TYPE_LST,blank=True,null=True)

    def save(self, *args, **kwargs):
        if self.rate_amount == 0:
            self.payment_type = None #ignore payment type if rate_amount is zero

        if self.rate_amount != 0 and self.payment_type == None:
            raise DataError #enforce that payment_type is not null when rate_amount is not zero
            
        super(Attendance, self).save(*args, **kwargs)        

    def __str__(self):
        return str(self.event) + ' - ' + str(self.date_time) + ' - ' + str(self.member)        

class Default_rate(models.Model):
    rate_type = models.IntegerField(choices=Event_rate.DANCE_RATE_LST,unique=True)
    rate_amount = models.DecimalField(max_digits=5, decimal_places=2)            