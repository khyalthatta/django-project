from django import forms


class AnnuityForm(forms.Form):
    VALUE_SIGN = (
        ('f', 'Future'),
        ('p', 'Present')
    )

    ANNUITY_SIGN = (
        ('o', 'Ordinary'),
        ('d', 'Due')
    )

    payment = forms.DecimalField(
        widget=forms.NumberInput(attrs={'class': 'form-control mb-2'})
    )

    rate = forms.DecimalField(
        widget=forms.NumberInput(attrs={'class': 'form-control mb-2'})
    )

    year = forms.DecimalField(
        widget=forms.NumberInput(attrs={'class': 'form-control mb-2'})
    )

    value = forms.ChoiceField(choices=VALUE_SIGN, widget=forms.Select(
        attrs={'class': 'form-control mb-2'}))

    annuity = forms.ChoiceField(
        choices=ANNUITY_SIGN, widget=forms.Select(attrs={'class': 'form-control mb-2'}))


class CompoundForm(forms.Form):

    PERIOD_CH = (
        ('1', 'Annual'),
        ('2', 'Semi-Annual'),
        ('3', 'Quarter'),
        ('4', 'Months'),
    )

    investment = forms.DecimalField(
        widget=forms.NumberInput(attrs={'class': 'form-control my-2'}),
        max_digits=100, decimal_places=2
    )

    rate = forms.DecimalField(
        widget=forms.NumberInput(attrs={'class': 'form-control my-2'}),
        max_digits=100, decimal_places=2
    )

    year = forms.IntegerField(
        widget=forms.NumberInput(attrs={'class': 'form-control my-2'})
    )

    period = forms.ChoiceField(
        widget=forms.Select(attrs={'class': 'form-control my-2'}),
        choices=PERIOD_CH
    )


class AmortizedForm(forms.Form):

    interest = forms.DecimalField(
        widget=forms.NumberInput(attrs={'class': 'form-control my-2'}),
        max_digits=100, decimal_places=2
    )

    years = forms.IntegerField(
        widget=forms.NumberInput(attrs={'class': 'form-control my-2'})
    )

    pva = forms.DecimalField(
        widget=forms.NumberInput(attrs={'class': 'form-control my-2'}),
        max_digits=100, decimal_places=2, label="Borrow Amount"
    )
