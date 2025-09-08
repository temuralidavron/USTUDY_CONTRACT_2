from django import forms
from .models import Contract
from django import forms
from django.core.exceptions import ValidationError


class ContractForm(forms.ModelForm):
    signature_data = forms.CharField(widget=forms.HiddenInput(), required=False)

    class Meta:
        model = Contract

        fields = [
            "course_type",
            "full_name",
            "age",
            "address",
            "document_type",
            "document_series",
            "jshshir",
            "document_given_by",
            "document_given_date",
            "parent_full_name",
            "parent_document_series",
            "parent_jshshir",
            "parent_document_given_by",
            "parent_document_given_date",
            "is_confirmed",
            "signature",

        ]
        widgets = {
            "document_given_date": forms.DateInput(attrs={"type": "date"}),
            "parent_document_given_date": forms.DateInput(attrs={"type": "date"}),
        }

    def clean(self):
        cleaned_data = super().clean()
        doc_type = cleaned_data.get("document_type")

        if doc_type == "metrka":  # faqat metrka bo‘lsa ota-ona majburiy
            required_fields = [
                "parent_full_name",
                "parent_document_series",
                "parent_jshshir",
                "parent_document_given_by",
                "parent_document_given_date",
            ]
            for field in required_fields:
                if not cleaned_data.get(field):
                    self.add_error(field, "Ushbu maydon majburiy.")
        return cleaned_data

# class ContractForm(forms.ModelForm):
#     class Meta:
#         model = Contract
#         fields = [
#             "course_type",
#             "full_name",
#             "age",
#             "address",
#             "document_type",
#             "document_series",
#             "jshshir",
#             "document_given_by",
#             "document_given_date",
#             "parent_full_name",
#             "parent_document_series",
#             "parent_jshshir",
#             "parent_document_given_by",
#             "parent_document_given_date",
#             "is_confirmed",
#         ]
#
#         widgets = {
#             "document_given_date": forms.DateInput(attrs={"type": "date"}),
#             "parent_document_given_date": forms.DateInput(attrs={"type": "date"}),
#         }
#     signature_data = forms.CharField(widget=forms.HiddenInput(), required=False)  # JS yuboradi
#
#     def clean_age(self):
#         age = self.cleaned_data.get("age")
#         if age is not None and age < 0:
#             raise ValidationError("Yosh manfiy bo'lishi mumkin emas.")
#         return age
#

class AdminContractForm(forms.ModelForm):
    class Meta:
        model = Contract
        fields = [
            'monthly_duration',
        ]


class PriceDurationForm(forms.Form):
    price = forms.IntegerField(
        label="Har oylik narx (so'm)",
        min_value=0,
        required=True,
        widget=forms.NumberInput(attrs={'class': 'form-control'})
    )

    monthly_duration = forms.IntegerField(
        label="Kurs muddati (oy)",
        min_value=1,
        required=True,
        widget=forms.NumberInput(attrs={'class': 'form-control'})
    )

class ContractAdminForm(forms.ModelForm):
    class Meta:
        model = Contract
        fields = [

            "initial_price",
            'price',
            'contract_number',
            "monthly_duration",
            'saved'
        ]

        labels = {
            'price': "Har oylik narx (so'm)",
            'monthly_duration': "Kurs muddati (oy)",
        }
        widgets = {
            'price': forms.NumberInput(attrs={'class': 'form-control'}),
            'monthly_duration': forms.NumberInput(attrs={'class': 'form-control'}),
        }


    def __init__(self, *args, **kwargs):
        super(ContractAdminForm, self).__init__(*args, **kwargs)
        for field in self.fields.values():
            field.required = True