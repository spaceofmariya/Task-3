import datetime

from django.db import models



GENDER = (
    ('', 'Select Gender'),
    ('M', 'Male'),
    ('F', 'Female'),
    ('O', 'Other')
)

CLASS = (
    ('','select'),
    ('1','1'),
    ('2', '2'),
    ('3','3'),
    ('4','4'),
    ('5','5'),
    ('6','6'),
    ('7','7'),
    ('8','8'),
    ('9','9'),
    ('10','10'),
    ('11','11'),
    ('12','12')
)

ITEMS = (
    ('','select 1 item'),
    ('1','Painting: Crayons'),
    ('2','Pencil Drawing'),
    ('3','Painting: Water Colour'),
    ('4','Cartoon'),
    ('5','Elocution Malayalam'),
    ('6','Elocution English'),
    ('7','Elocution Hindi'),
    ('8','Recitation Malayalam'),
    ('9','Recitation English'),
    ('10','Recitation Hindi'),
    ('11','Essay Writing English'),
    ('12','Essay Writing Malayalam'),
    ('13','Light Music'),
    ('14','Classical Music'),
    ('15','Mappilapattu'),
    ('16','Monoact'),
    ('17','Mimicry'),
    ('18','Folk Dance'),
    ('19','Bharathanatyam'),
    ('20','Mohiniyattam'),
    ('21','Guitar'),
    ('22','Key Board-Western'),
    ('23','Tabala-Eastern'),
    ('24','Group Song'),
    ('25','Group Dance')
)

class Form(models.Model):
    first_name = models.CharField(max_length=120)
    last_name = models.CharField(max_length=120)
    date_of_birth = models.DateField(default=datetime.date.today())
    gender = models.CharField(max_length=120,choices=GENDER)
    school_grade = models.CharField(max_length=120,choices=CLASS)
    email = models.EmailField(unique=True)
    contact_number = models.CharField(max_length=10)
    item = models.CharField(max_length=120,choices=ITEMS)
    
    def __str__(self):
        return str(self.first_name)
