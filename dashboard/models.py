from django.db import models

# Create your models here.
CATEGORY = (
    ('I-II', 'I-II'),
    ('III', 'III'),
    ('IV', 'IV'),
    ('V', 'V'),
    ('VI', 'VI'),
)

CATEGORY1 = (
    ('CS','CS'),
    ('IT','IT'),
    ('EXTC','EXTC'),
    ('Mech','Mech'),
    ('Civil','Civil'),
)

CATEGORY2 = (
    ('Placement','Placement'),
    ('Higher Studies','Higher Studies'),
)

class Students(models.Model):
    prn = models.CharField(max_length=10, null=True)
    name = models.CharField(max_length=100, null=True)
    branch = models.CharField(max_length=5, choices=CATEGORY1, null=True)
    dob = models.DateField(null=True)
    email_id1 = models.CharField(max_length=100, null=True)
    email_id2 = models.CharField(max_length=100, null=True, blank=True)
    phone1 = models.IntegerField(null=True, blank=False)
    phone2 = models.IntegerField(null=True,blank=True)
    address = models.CharField(max_length=1000, null=True)
    tenth_board = models.CharField(max_length=15, null=True)
    tenth_perc = models.FloatField(null=True)
    tenth_year = models.IntegerField(null=True)
    twelth_board = models.CharField(max_length=15, null=True)
    twelth_perc = models.FloatField(null=True)
    twelth_year = models.IntegerField(null=True)
    diploma_board = models.CharField(max_length=15, null=True, blank=True)
    diploma_perc = models.FloatField(null=True, blank=True)
    diploma_year = models.FloatField(null=True, blank=True)
    sem1 = models.FloatField(null=True, blank=True)
    sem2 = models.FloatField(null=True, blank=True)
    sem3 = models.FloatField(null=True, blank=True)
    sem4 = models.FloatField(null=True, blank=True)
    sem5 = models.FloatField(null=True, blank=True)
    sem6 = models.FloatField(null=True, blank=True)
    cgpi = models.FloatField(null=True, blank=True)
    perc = models.FloatField(null=True, blank=True)
    live_kts = models.IntegerField(null=True, blank=True)
    dead_kts = models.IntegerField(null=True, blank=True)
    choice = models.CharField(max_length=15, choices=CATEGORY2, null=True)


    def __str__(self):
        return f'{self.prn}-{self.name}-{self.branch}-{self.dob}-{self.email_id1}-{self.email_id2}-{self.phone1}-{self.phone2}{self.address}-{self.tenth_board}-{self.tenth_perc}-{self.tenth_year}{self.twelth_board}-{self.twelth_perc}-{self.twelth_year}-{self.diploma_board}{self.diploma_perc}-{self.diploma_year}-{self.sem1}-{self.sem2}{self.sem3}-{self.sem4}-{self.sem5}-{self.sem6}{self.cgpi}-{self.perc}-{self.live_kts}-{self.dead_kts}-{self.choice}'

#Placements
class Placements(models.Model):
    prn = models.CharField(max_length=10, null=True)
    name = models.CharField(max_length=100, null=True)
    offer1 = models.CharField(max_length=100, null=True)
    offer2 = models.CharField(max_length=100, null=True)
    offer3 = models.CharField(max_length=100, null=True)
    batch = models.CharField(max_length=10, null=True)

    def __str__(self):
        return f'{self.prn}-{self.name}-{self.offer1}-{self.offer2}-{self.offer3}-{self.batch}'


#Companies
class Companies(models.Model):
    company = models.CharField(max_length=100, null=True)
    salary = models.FloatField(null = True)

    def __str__(self):
        return f'{self.company}-{self.salary}'


#Bulletin Board
class Bulletin(models.Model):
    notice = models.CharField(max_length=1000, null=True)

    def __str__(self):
        return f'{self.notice}'


class Marks(models.Model):
    branch = models.CharField(max_length=5, choices=CATEGORY1, null=True)
    sem = models.CharField(max_length=5, choices=CATEGORY, null=True)
    file = models.FileField(upload_to='marksheets')

    def __str__(self):
        return f'{self.branch}-{self.sem}'