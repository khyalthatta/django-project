from django.shortcuts import render

from .form import AnnuityForm, CompoundForm, AmortizedForm


def annuity_view(request, *args, **kwargs):
    form = AnnuityForm()
    result = ''
    if request.method == "POST":
        form = AnnuityForm(request.POST)
        if form.is_valid():
            payment = form.cleaned_data['payment']
            rate = form.cleaned_data['rate']
            year = form.cleaned_data['year']
            rate = rate/100

            def calc_annuity(payment, rate, year):

                value = form.cleaned_data['value']
                if value.lower() == 'p':
                    annuity = form.cleaned_data['annuity']

                    if annuity.lower() == 'o':
                        ordinary_annuity = payment * ((1 - (1 / (1 + rate) ** year))/rate)
                        return ordinary_annuity

                    elif annuity.lower() == 'd':
                        annuity_due = payment * ((1 - (1 / (1 + rate) ** year))/rate) * (1 + rate)

                        return annuity_due
                    else:
                        return "The keyword you have passed is wrong. Please try with right one."

                elif value.lower() == 'f':

                    annuity = form.cleaned_data['annuity']

                    if annuity.lower() == 'o':
                        ordinary_annuity = payment * (((1 + rate) ** year)-1)/rate
                        return ordinary_annuity

                    elif annuity.lower() == 'd':
                        annuity_due = payment * (((1 + rate) ** year)-1)/rate * (1 + rate)
                        return annuity_due

                    else:
                        return "The keyword you have passed is wrong. Please try with right one."

                else:
                    return "You have to type the keyword correctly."

            result = f"{calc_annuity(payment, rate, year): .2f}"
            form = AnnuityForm()
    context = {
        'form': form,
        'result': result
    }
    return render(request, 'finance/annuity.html', context)


def compound_view(request, *args, **kwargs):
    form = CompoundForm()
    result = ''
    if request.method == "POST":
        form = CompoundForm(request.POST)
        if form.is_valid():
            investment = form.cleaned_data['investment']
            rate = form.cleaned_data['rate']
            year = form.cleaned_data['year']
            period = form.cleaned_data['period']

            def calc_compound(investment, rate, year):
                if period == '1':
                    compound_interest = investment * (1 + rate/100) ** year
                    return compound_interest

                elif period == '2':
                    compound_interest = investment * (1 + rate/(100*2)) ** (year*2)
                    return compound_interest

                elif period == '3':
                    compound_interest = investment * (1 + rate/(100*4)) ** (year*4)
                    return compound_interest

                elif period == '4':
                    compound_interest = investment * (1 + rate/(100*12)) ** (year*12)
                    return compound_interest

                else:
                    return "Not determined due to the wrong period."

            result = calc_compound(investment, rate, year)
            form = CompoundForm()

    context = {
        'form': form,
        'result': result
    }
    return render(request, 'finance/compound.html', context)


def amortized_view(request, *args, **kwargs):

    form = AmortizedForm()
    output = []
    submit = request.POST.get('submit')
    if request.method == "POST":
        form = AmortizedForm(request.POST)
        if form.is_valid():
            i = form.cleaned_data['interest']/100
            n = form.cleaned_data['years']
            pva = form.cleaned_data['pva']

            pvifa = (1 - (1 / (1 + i) ** n))/i
            pmt = pva / pvifa

            def amortized_table(pmt, i, n, pva):
                total_interest = 0
                principal_list = []
                interest_list = []

                for num in range(0, n+1):

                    if num == 0:
                        output.append(f"""<td>{num}</td>
                                         <td>0</td>
                                         <td>0</td>
                                         <td>0</td>
                                         <td>{pva}</td>""")
                    else:
                        # Step 2 : Find  the interest paid in year 1
                        interest = pva * i
                        interest_list.append(interest)
                        # Step 3 : Find  the principal re-paid in year 1
                        principal = pmt - interest
                        principal_list.append(principal)

                        # Step 4 : Find  the ending balance after year 1
                        loan_bal = pva - principal

                        output.append(f""" <td>{num}</td>
                                           <td>{pmt:.2f}</td>
                                           <td>{interest:.2f}</td>
                                           <td>{principal:.2f}</td>
                                           <td>{loan_bal:.2f}</td>""")

                        pva = loan_bal

                        total_interest += interest

            amortized_table(pmt, i, n,  pva)

    context = {
        'form': form,
        'output': output,
        'activated': submit
    }

    return render(request, 'finance/amortized.html', context)
