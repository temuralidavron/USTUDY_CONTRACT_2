from django.db import models
from django.conf import settings

class CourseType(models.TextChoices):
    BACKEND = 'backend', 'Backend'
    FRONTEND = 'frontend', 'Frontend'
    DATA_SCIENCE = 'data_science', 'Data Science'
    CYBER_SECURITY = 'cyber_security', 'Cyber Security'
    GRAPHIC_DESIGN = 'graphic_design', 'Graphic Design'
    MOTION_DESIGN = 'motion_design', 'Motion Design'
    IT_KIDS_3 = 'it_kids_3', 'IT for KIDS (3 oylik)'
    IT_KIDS_17 = 'it_kids_17', 'IT for KIDS (17 oylik)'

class DocumentType(models.TextChoices):
    PASSPORT = 'passport', 'Passport'
    METRIKA = 'metrka', 'Birth Certificate'

class Contract(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    course_type = models.CharField(max_length=20, choices=CourseType.choices)
    full_name = models.CharField(max_length=255)
    phone = models.CharField(max_length=13)
    age = models.PositiveIntegerField()
    address = models.TextField()

    document_type = models.CharField(
        max_length=10, choices=DocumentType.choices, blank=True, null=True
    )
    document_series = models.CharField(max_length=30, blank=True, null=True)
    jshshir = models.CharField(max_length=20, blank=True, null=True)
    document_given_by = models.CharField(max_length=255, blank=True, null=True)
    document_given_date = models.DateField(blank=True, null=True)

    parent_full_name = models.CharField(max_length=255, blank=True, null=True)
    parent_document_series = models.CharField(max_length=30, blank=True, null=True)
    parent_jshshir = models.CharField(max_length=20, blank=True, null=True)
    parent_document_given_by = models.CharField(max_length=255, blank=True, null=True)
    parent_document_given_date = models.DateField(blank=True, null=True)

    is_confirmed = models.BooleanField(default=False)
    saved=models.BooleanField(default=False)
    initial_price = models.DecimalField(max_digits=10, decimal_places=2,blank=True,null=True)  # dastlabki narx
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    price = models.DecimalField(max_digits=10, decimal_places=2,blank=True, null=True)
    contract_number = models.PositiveIntegerField(blank=True, null=True)
    monthly_duration = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    signature = models.ImageField(upload_to="signatures/", blank=True, null=True)  # migrate qilish kerak



    def __str__(self):
        return f"{self.user.username} - {self.course_type}"
