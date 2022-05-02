from django import forms


class CalculatorForm(forms.Form):
    SIGNS = (
        ('+', 'ADD'),
        ('-', 'SUB'),
        ('*', 'MUL'),
        ('/', 'DIV')
    )
    num1 = forms.DecimalField(
        widget=forms.NumberInput(attrs={'class': 'form-control mb-2'}),
        max_digits=100, decimal_places=2,
    )

    num2 = forms.DecimalField(
        widget=forms.NumberInput(attrs={'class': 'form-control mb-2'}),
        max_digits=100, decimal_places=2,
    )

    opt = forms.ChoiceField(choices=SIGNS)
