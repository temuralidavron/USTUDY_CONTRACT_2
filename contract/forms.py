from django import forms
from .models import Contract


class ContractForm(forms.ModelForm):
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
        ]
        widgets = {
            "document_given_date": forms.DateInput(attrs={"type": "date"}),
            "parent_document_given_date": forms.DateInput(attrs={"type": "date"}),
        }


class AdminContractForm(forms.ModelForm):
    class Meta:
        model = Contract
        fields = [
            'monthly_price'
        ]
