from unicodedata import name
from django.db import models
from multiselectfield import MultiSelectField
from django.core.validators import FileExtensionValidator

# Create your models here.

class Process_data(models.Model):
    pipeline_choices = (
        ('Engine-1','engine_1'),
        ('Engine-2','engine_2'),
        ('Engine-3','engine_3'),
        ('Engine-4','engine_4'),
    )
    classification_model_choices = (
        ('Yes','yes'),
        ('No','no'),
    )

    TIMEZONE_CHOICES=(
    ('UTC-12:00, International Date Line West', '(UTC-12:00) International Date Line West'),
    ('UTC-11:00, Coordinated Universal Time-11','(UTC-11:00) Coordinated Universal Time-11'),
    ('UTC-10:00, Aleutian Islands','(UTC-10:00) Aleutian Islands'),
    ('UTC-10:00, Hawaii','(UTC-10:00) Hawaii'),
    ('UTC-09:30, Marquesas Islands','(UTC-09:30) Marquesas Islands'),
    ('UTC-09:00, Alaska','(UTC-09:00) Alaska'),
    ('UTC-09:00, Coordinated Universal Time-09','(UTC-09:00) Coordinated Universal Time-09'),
    ('UTC-08:00, Baja California','(UTC-08:00) Baja California'),
    ('UTC-08:00, Coordinated Universal Time-08','(UTC-08:00) Coordinated Universal Time-08'),
    ('UTC-08:00, Pacific Time (US & Canada)','(UTC-08:00) Pacific Time (US & Canada)'),
    ('UTC-07:00, Arizona','(UTC-07:00) Arizona'),
    ('UTC-07:00, Chihuahua, La Paz, Mazatlan','(UTC-07:00) Chihuahua, La Paz, Mazatlan'),
    ('UTC-07:00, Mountain Time (US & Canada)','(UTC-07:00) Mountain Time (US & Canada)'),
    ('UTC-06:00, Central America','(UTC-06:00) Central America'),
    ('UTC-06:00, Central Time (US & Canada)','(UTC-06:00) Central Time (US & Canada)'),
    ('UTC-06:00, Easter Island','(UTC-06:00) Easter Island'),
    ('UTC-06:00, Guadalajara, Mexico City, Monterrey','(UTC-06:00) Guadalajara, Mexico City, Monterrey'),
    ('UTC-06:00, Saskatchewan','(UTC-06:00) Saskatchewan'),
    ('UTC-05:00, Bogota, Lima, Quito, Rio Branco','(UTC-05:00) Bogota, Lima, Quito, Rio Branco'),
    ('UTC-05:00, Chetumal','(UTC-05:00) Chetumal'),
    ('UTC-05:00, Eastern Time (US & Canada)','(UTC-05:00) Eastern Time (US & Canada)'),
    ('UTC-05:00, Haiti','(UTC-05:00) Haiti'),
    ('UTC-05:00, Havana','(UTC-05:00) Havana'),
    ('UTC-05:00, Indiana (East)','(UTC-05:00) Indiana (East)'),
    ('UTC-05:00, Turks and Caicos','(UTC-05:00) Turks and Caicos'),
    ('UTC-04:00, Asuncion','(UTC-04:00) Asuncion'),
    ('UTC-04:00, Atlantic Time (Canada)','(UTC-04:00) Atlantic Time (Canada)'),
    ('UTC-04:00, Caracas','(UTC-04:00) Caracas'),
    ('UTC-04:00, Cuiaba','(UTC-04:00) Cuiaba'),
    ('UTC-04:00, Georgetown, La Paz, Manaus, San Juan','(UTC-04:00) Georgetown, La Paz, Manaus, San Juan'),
    ('UTC-04:00, Santiago','(UTC-04:00) Santiago'),
    ('UTC-03:30, Newfoundland','(UTC-03:30) Newfoundland'),
    ('UTC-03:00, Araguaina','(UTC-03:00) Araguaina'),
    ('UTC-03:00, Brasilia','(UTC-03:00) Brasilia'),
    ('UTC-03:00, Cayenne, Fortaleza','(UTC-03:00) Cayenne, Fortaleza'),
    ('UTC-03:00, City of Buenos Aires','(UTC-03:00) City of Buenos Aires'),
    ('UTC-03:00, Greenland','(UTC-03:00) Greenland'),
    ('UTC-03:00, Montevideo','(UTC-03:00) Montevideo'),
    ('UTC-03:00, Punta Arenas','(UTC-03:00) Punta Arenas'),
    ('UTC-03:00, Saint Pierre and Miquelon','(UTC-03:00) Saint Pierre and Miquelon'),
    ('UTC-03:00, Salvador','(UTC-03:00) Salvador'),
    ('UTC-02:00, Coordinated Universal Time-02','(UTC-02:00) Coordinated Universal Time-02'),
    ('UTC-01:00, Azores','(UTC-01:00) Azores'),
    ('UTC-01:00, ','(UTC-01:00) Cabo Verde Is.'),
    ('UTC, Coordinated Universal Time','(UTC) Coordinated Universal Time'),
    ('UTC+00:00, Dublin, Edinburgh, Lisbon, London','(UTC+00:00) Dublin, Edinburgh, Lisbon, London'),
    ('UTC+00:00, Monrovia, Reykjavik','(UTC+00:00) Monrovia, Reykjavik'),
    ('UTC+00:00, Sao Tome','(UTC+00:00) Sao Tome'),
    ('UTC+01:00, Casablanca','(UTC+01:00) Casablanca'),
    ('UTC+01:00, Amsterdam, Berlin, Bern, Rome, Stockholm, Vienna','(UTC+01:00) Amsterdam, Berlin, Bern, Rome, Stockholm, Vienna'),
    ('UTC+01:00, Belgrade, Bratislava, Budapest, Ljubljana, Prague','(UTC+01:00) Belgrade, Bratislava, Budapest, Ljubljana, Prague'),
    ('UTC+01:00, Brussels, Copenhagen, Madrid, Paris','(UTC+01:00) Brussels, Copenhagen, Madrid, Paris'),
    ('UTC+01:00, Sarajevo, Skopje, Warsaw, Zagreb','(UTC+01:00) Sarajevo, Skopje, Warsaw, Zagreb'),
    ('UTC+01:00, West Central Africa','(UTC+01:00) West Central Africa'),
    ('UTC+02:00, Amman','(UTC+02:00) Amman'),
    ('UTC+02:00, Athens, Bucharest','(UTC+02:00) Athens, Bucharest'),
    ('UTC+02:00, Beirut','(UTC+02:00) Beirut'),
    ('UTC+02:00, Cairo','(UTC+02:00) Cairo'),
    ('UTC+02:00, Chisinau','(UTC+02:00) Chisinau'),
    ('UTC+02:00, Damascus','(UTC+02:00) Damascus'),
    ('UTC+02:00, Gaza, Hebron','(UTC+02:00) Gaza, Hebron'),
    ('UTC+02:00, Harare, Pretoria','(UTC+02:00) Harare, Pretoria'),
    ('UTC+02:00, Helsinki, Kyiv, Riga, Sofia, Tallinn, Vilnius','(UTC+02:00) Helsinki, Kyiv, Riga, Sofia, Tallinn, Vilnius'),
    ('UTC+02:00, Jerusalem','(UTC+02:00) Jerusalem'),
    ('UTC+02:00, Kaliningrad','(UTC+02:00) Kaliningrad'),
    ('UTC+02:00, Khartoum','(UTC+02:00) Khartoum'),
    ('UTC+02:00, Tripoli','(UTC+02:00) Tripoli'),
    ('UTC+02:00, Windhoek','(UTC+02:00) Windhoek'),
    ('UTC+03:00, Baghdad','(UTC+03:00) Baghdad'),
    ('UTC+03:00, Istanbul','(UTC+03:00) Istanbul'),
    ('UTC+03:00, Kuwait, Riyadh','(UTC+03:00) Kuwait, Riyadh'),
    ('UTC+03:00, Minsk','(UTC+03:00) Minsk'),
    ('UTC+03:00, Moscow, St. Petersburg','(UTC+03:00) Moscow, St. Petersburg'),
    ('UTC+03:00, Nairobi','(UTC+03:00) Nairobi'),
    ('UTC+03:30, Tehran','(UTC+03:30) Tehran'),
    ('UTC+04:00, Abu Dhabi, Muscat','(UTC+04:00) Abu Dhabi, Muscat'),
    ('UTC+04:00, Astrakhan, Ulyanovsk','(UTC+04:00) Astrakhan, Ulyanovsk'),
    ('UTC+04:00, Baku','(UTC+04:00) Baku'),
    ('UTC+04:00, Izhevsk, Samara','(UTC+04:00) Izhevsk, Samara'),
    ('UTC+04:00, Port Louis','(UTC+04:00) Port Louis'),
    ('UTC+04:00, Saratov','(UTC+04:00) Saratov'),
    ('UTC+04:00, Tbilisi','(UTC+04:00) Tbilisi'),
    ('UTC+04:00, Volgograd','(UTC+04:00) Volgograd'),
    ('UTC+04:00, Yerevan','(UTC+04:00) Yerevan'),
    ('UTC+04:30, Kabul','(UTC+04:30) Kabul'),
    ('UTC+05:00, Ashgabat, Tashkent','(UTC+05:00) Ashgabat, Tashkent'),
    ('UTC+05:00, Ekaterinburg','(UTC+05:00) Ekaterinburg'),
    ('UTC+05:00, Islamabad, Karachi','(UTC+05:00) Islamabad, Karachi'),
    ('UTC+05:00, Qyzylorda','(UTC+05:00) Qyzylorda'),
    ('UTC+05:30, Chennai, Kolkata, Mumbai, New Delhi','(UTC+05:30) Chennai, Kolkata, Mumbai, New Delhi'),
    ('UTC+05:30, Sri Jayawardenepura','(UTC+05:30) Sri Jayawardenepura'),
    ('UTC+05:45, Kathmandu','(UTC+05:45) Kathmandu'),
    ('UTC+06:00, Astana','(UTC+06:00) Astana'),
    ('UTC+06:00, Dhaka','(UTC+06:00) Dhaka'),
    ('UTC+06:00, Omsk','(UTC+06:00) Omsk'),
    ('UTC+06:30, Yangon (Rangoon)','(UTC+06:30) Yangon (Rangoon)'),
    ('UTC+07:00, Bangkok, Hanoi, Jakarta','(UTC+07:00) Bangkok, Hanoi, Jakarta'),
    ('UTC+07:00, Barnaul, Gorno-Altaysk','(UTC+07:00) Barnaul, Gorno-Altaysk'),
    ('UTC+07:00, Hovd','(UTC+07:00) Hovd'),
    ('UTC+07:00, Krasnoyarsk','(UTC+07:00) Krasnoyarsk'),
    ('UTC+07:00, Novosibirsk','(UTC+07:00) Novosibirsk'),
    ('UTC+07:00, Tomsk','(UTC+07:00) Tomsk'),
    ('UTC+08:00, Beijing, Chongqing, Hong Kong, Urumqi','(UTC+08:00) Beijing, Chongqing, Hong Kong, Urumqi'),
    ('UTC+08:00, Irkutsk','(UTC+08:00) Irkutsk'),
    ('UTC+08:00, Kuala Lumpur, Singapore','(UTC+08:00) Kuala Lumpur, Singapore'),
    ('UTC+08:00, Perth','(UTC+08:00) Perth'),
    ('UTC+08:00, Taipei','(UTC+08:00) Taipei'),
    ('UTC+08:00, Ulaanbaatar','(UTC+08:00) Ulaanbaatar'),
    ('UTC+08:45, Eucla','(UTC+08:45) Eucla'),
    ('UTC+09:00, Chita','(UTC+09:00) Chita'),
    ('UTC+09:00, Osaka, Sapporo, Tokyo','(UTC+09:00) Osaka, Sapporo, Tokyo'),
    ('UTC+09:00, Pyongyang','(UTC+09:00) Pyongyang'),
    ('UTC+09:00, Seoul','(UTC+09:00) Seoul'),
    ('UTC+09:00, Yakutsk','(UTC+09:00) Yakutsk'),
    ('UTC+09:30, Adelaide','(UTC+09:30) Adelaide'),
    ('UTC+09:30, Darwin','(UTC+09:30) Darwin'),
    ('UTC+10:00, Brisbane','(UTC+10:00) Brisbane'),
    ('UTC+10:00, Canberra, Melbourne, Sydney','(UTC+10:00) Canberra, Melbourne, Sydney'),
    ('UTC+10:00, Guam, Port Moresby','(UTC+10:00) Guam, Port Moresby'),
    ('UTC+10:00, Hobart','(UTC+10:00) Hobart'),
    ('UTC+10:00, Vladivostok','(UTC+10:00) Vladivostok'),
    ('UTC+10:30, Lord Howe Island','(UTC+10:30) Lord Howe Island'),
    ('UTC+11:00, Bougainville Island','(UTC+11:00) Bougainville Island'),
    ('UTC+11:00, Chokurdakh','(UTC+11:00) Chokurdakh'),
    ('UTC+11:00, Magadan','(UTC+11:00) Magadan'),
    ('UTC+11:00, Norfolk Island','(UTC+11:00) Norfolk Island'),
    ('UTC+11:00, Sakhalin','(UTC+11:00) Sakhalin'),
    ('UTC+11:00, Solomon Is., New Caledonia','(UTC+11:00) Solomon Is., New Caledonia'),
    ('UTC+12:00, Anadyr, Petropavlovsk-Kamchatsky','(UTC+12:00) Anadyr, Petropavlovsk-Kamchatsky'),
    ('UTC+12:00, Auckland, Wellington','(UTC+12:00) Auckland, Wellington'),
    ('UTC+12:00, Coordinated Universal Time+12','(UTC+12:00) Coordinated Universal Time+12'),
    ('UTC+12:00, Fiji','(UTC+12:00) Fiji'),
    ('UTC+12:45, Chatham Islands','(UTC+12:45) Chatham Islands'),
    ('UTC+13:00, Coordinated Universal Time+13','(UTC+13:00) Coordinated Universal Time+13'),
    ('UTC+13:00, Nuku’alofa','(UTC+13:00) Nuku’alofa'),
    ('UTC+13:00, Samoa','(UTC+13:00) Samoa'),
    ('UTC+14:00, Kiritimati Island','(UTC+14:00) Kiritimati Island'),
)

    process_sla_choices = (
        ('1','1'),
        ('2','2'),
        ('3','3'),
        ('4','4'),
        ('5','5'),
        ('6','6'),
        ('7','7'),
        ('8','8'),
        ('9','9'),
        ('10','10'),
    )
    
    pre_processing_choices = (
        ('yes','yes'),
        ('no','no'),
       
    )
    Input_documents_choices = (
        ('JPG','JPG'),
        ('PDF','PDF'),
        ('JPEG','JPEG'),
        ('TIF','TIF'),
        ('PNG','PNG'),
       
    )

    Input_documents = MultiSelectField(choices=Input_documents_choices,null=True)
    pre_processing = models.CharField(max_length=50, choices=pre_processing_choices,null=True)
    pipeline = models.CharField(max_length=50, choices=pipeline_choices,null=True)
    classification_model = models.CharField(max_length=50, choices=classification_model_choices,null=True)
    time_zone = models.CharField(max_length=500, choices=TIMEZONE_CHOICES,null=True)
    process_sla = models.CharField(max_length=50, choices=process_sla_choices,null=True)

    process_name = models.CharField(max_length=50,null=True)
    def __str__(self):
        return self.process_name



class Cnn_model(models.Model):
    type_coices = (
        ('Regular_Model','Regular_Model'),
        ('VCG_Model','VCG_Model'),
        
    )
    epochs_choices = (
        ('20','20'),
        ('30','30'),
        ('40','40'),
        ('50','50'),
        ('60','60'),
        ('70','70'),
        ('80','80'),
        ('90','90'),
        ('100','100'),
        
    )
    batch_choices = (
        ('16','16'),
        ('32','32'),
        ('64','64'),
        
    )
    kernel_Initializer_choices = (
        ('he_noraml','he_noraml'),
        ('he_uniform','he_uniform'),
        
    )
    optimize_choices = (
        ('rmsprop','rmsprop'),
        ('xrmprop','xrmprop'),
        
    )
    test_size_choices = (
        ('05','05'),
        ('06','06'),
        ('07','07'),
        ('08','08'),
        
    )
    activation_choices = (
        ('relu','relu'),
        ('esl','esl'),
        
    )

    type = models.CharField(max_length=50, choices=type_coices,null=True)
    activation = models.CharField(max_length=50, choices=activation_choices,null=True)
    test_size = models.CharField(max_length=50, choices=test_size_choices,null=True)
    epochs = models.CharField(max_length=50, choices=epochs_choices,null=True)
    Batch = models.CharField(max_length=50, choices=batch_choices,null=True)
    kernel_Initializer = models.CharField(max_length=50, choices=kernel_Initializer_choices,null=True)
    optimize = models.CharField(max_length=50, choices=optimize_choices,null=True)
    cofidence_number = models.CharField(max_length=50,null=True)
    name = models.CharField(max_length=50,null=True)
    cnnclass = models.CharField(max_length=50,default="Single_Class")
    sample_file = models.FileField(null=True)
   
    def __str__(self):
        return self.name


class auth_user(models.Model):
    user_type_choices = (
        ('client','client'),
        ('none','none'),
        
    )

    user_type= models.CharField(max_length=50, choices=user_type_choices,null=True)
