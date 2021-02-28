from django.contrib import admin

# Register your models here.
from .models import careers,signups,telephone_tech_support,video_tech_support,one_on_one_online_session,QueryPages,JsonData,Online_Gd_For_Admin,Online_Gd_For_user

class careersadmin(admin.ModelAdmin):
	list_display=['expert_name','expert_email','expert_phone_number','resume_url','background','subject','description']
admin.site.register(careers,careersadmin)

class signupsadmin(admin.ModelAdmin):
	list_display=['user','mobile_no','address','country','state','Postal_code']
admin.site.register(signups,signupsadmin)

class telephone_tech_supportadmin(admin.ModelAdmin):
	list_display=['user','query','slot']
admin.site.register(telephone_tech_support,telephone_tech_supportadmin)
class video_tech_supportadmin(admin.ModelAdmin):
	list_display=['user','query','slot']
admin.site.register(video_tech_support,video_tech_supportadmin)
class one_on_one_online_sessionadmin(admin.ModelAdmin):
	list_display=['user','query','slot']
admin.site.register(one_on_one_online_session,one_on_one_online_sessionadmin)
class QueryPageAdmin(admin.ModelAdmin):
	list_display=['question','answer_heading','youtube_link','article_link']
admin.site.register(QueryPages,QueryPageAdmin)
class JsonDataAdmin(admin.ModelAdmin):
	list_display=['all_data']
admin.site.register(JsonData,JsonDataAdmin)
class Online_Gd_For_Admins(admin.ModelAdmin):
	list_display=['gd_topic_name','date','time','number_of_paticipate']
admin.site.register(Online_Gd_For_Admin,Online_Gd_For_Admins)
class Online_Gd_For_users(admin.ModelAdmin):
	list_display=['user','select_date_time']
admin.site.register(Online_Gd_For_user,Online_Gd_For_users)