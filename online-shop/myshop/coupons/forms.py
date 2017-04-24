from django import forms


class CouponApplayForm(forms.Form):
    code = forms.CharField()
