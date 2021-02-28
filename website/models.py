from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class work_with_us(models.Model):
    expert_name = models.CharField(max_length=255)
    expert_email = models.EmailField(max_length=254)
    expert_phone_number = models.CharField(max_length=12)
    resume_url = models.FileField(upload_to='media/resume/')
    background = models.FileField(upload_to='media/background/')
    # resume_url=models.TextField()
    # background_url=models.TextField()
    subject = models.CharField(max_length=255)

    # description=models.TextField()

    def _str_(self):
        return self.title


class workwithus(models.Model):
    expert_name = models.CharField(max_length=255)
    expert_email = models.EmailField(max_length=254)
    expert_phone_number = models.CharField(max_length=12)
    resume_url = models.FileField(upload_to='media/resume/')
    background = models.FileField(upload_to='media/background/')
    # resume_url=models.TextField()
    # background_url=models.TextField()
    subject = models.CharField(max_length=255)


# description=models.TextField()

class careers(models.Model):
    expert_name = models.CharField(max_length=255)
    expert_email = models.EmailField(max_length=254)
    expert_phone_number = models.CharField(max_length=12)
    resume_url = models.FileField(upload_to='resume/')
    background = models.FileField(upload_to='background/')
    # resume_url=models.TextField()
    # background_url=models.TextField()
    subject = models.CharField(max_length=255)
    description = models.TextField()


class signups(models.Model):
    user = models.ForeignKey(User, related_name='signup', on_delete=models.CASCADE)
    mobile_no = models.CharField(max_length=12)
    address = models.CharField(max_length=500)
    country = models.CharField(max_length=20)
    state = models.CharField(max_length=20)
    Postal_code = models.CharField(max_length=7)


class telephone_tech_support(models.Model):
    user = models.ForeignKey(User, related_name='telephone_tech_support', on_delete=models.CASCADE, default=1)
    query = models.TextField()
    slot = models.CharField(max_length=160)


class video_tech_support(models.Model):
    user = models.ForeignKey(User, related_name='video_tech_support', on_delete=models.CASCADE, default=1)
    query = models.TextField()
    slot = models.CharField(max_length=160)


class one_on_one_online_session(models.Model):
    user = models.ForeignKey(User, related_name='one_on_one_online_session', on_delete=models.CASCADE, default=1)
    query = models.TextField()
    slot = models.CharField(max_length=160)


class QueryPages(models.Model):
    question = models.CharField(max_length=500)
    answer_heading = models.TextField()
    youtube_link = models.CharField(max_length=255)
    article_link = models.CharField(max_length=255)


from jsonfield import JSONField


class JsonData(models.Model):
    all_data = JSONField()


class Online_Gd_For_Admin(models.Model):
    gd_topic_name = models.CharField(max_length=500)
    date = models.DateField()
    time = models.TimeField()
    number_of_paticipate = models.IntegerField()


class Online_Gd_For_user(models.Model):
    user = models.ForeignKey(User, related_name='Online_Gd_For_user', on_delete=models.CASCADE, default=1)
    select_date_time = models.CharField(max_length=500)





