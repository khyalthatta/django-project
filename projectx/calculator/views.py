from django.shortcuts import render


from .form import CalculatorForm


def operation_view(request):
    form = CalculatorForm()
    result = ''
    if request.method == "POST":
        form = CalculatorForm(request.POST)
        if form.is_valid():
            first = form.cleaned_data['num1']
            second = form.cleaned_data['num2']
            ch = form.cleaned_data['opt']

            if ch == '+':
                result = first + second

            elif ch == '-':
                result = first - second

            elif ch == '*':
                result = first * second

            elif ch == '/':
                result = round(first / second, 2)

            form = CalculatorForm()

        else:
            print(form.errors)

    context = {
        'form': form,
        'result': result
    }
    return render(request, 'calculator/calculator.html', context)
