import datetime

from django.db import models


GENDER = (
    ('', 'select gender'),
    ('Male', 'Male'),
    ('Female', 'Female'),
    ('Other', 'Other')
)

CLASS = (
    ('','select class'),
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
    ('Painting: Crayons','Painting: Crayons'),
    ('Pencil Drawing','Pencil Drawing'),
    ('Painting: Water Colour','Painting: Water Colour'),
    ('Cartoon','Cartoon'),
    ('Elocution Malayalam','Elocution Malayalam'),
    ('Elocution English','Elocution English'),
    ('Elocution Hindi','Elocution Hindi'),
    ('Recitation Malayalam','Recitation Malayalam'),
    ('Recitation English','Recitation English'),
    ('Recitation Hindi','Recitation Hindi'),
    ('Essay Writing English','Essay Writing English'),
    ('Essay Writing Malayalam','Essay Writing Malayalam'),
    ('Light Music','Light Music'),
    ('Classical Music','Classical Music'),
    ('Mappilapattu','Mappilapattu'),
    ('Monoact','Monoact'),
    ('Mimicry','Mimicry'),
    ('Folk Dance','Folk Dance'),
    ('Bharathanatyam','Bharathanatyam'),
    ('Mohiniyattam','Mohiniyattam'),
    ('Guitar','Guitar'),
    ('Key Board-Western','Key Board-Western'),
    ('Tabala-Eastern','Tabala-Eastern'),
    ('Group Song','Group Song'),
    ('Group Dance','Group Dance')
)

class Form(models.Model):
    first_name = models.CharField(max_length=120)
    last_name = models.CharField(max_length=120)
    date_of_birth = models.DateField(default=datetime.date.today())
    gender = models.CharField(max_length=120,choices=GENDER)
    school_grade = models.CharField(max_length=120,choices=CLASS)
    email = models.EmailField()
    contact_number = models.CharField(max_length=10)
    item = models.CharField(max_length=120,choices=ITEMS)
    
    def __str__(self):
        return str(self.first_name)
