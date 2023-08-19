from django.shortcuts import render
from .models import Company, Job, Vehicle, Employee
from django.http import HttpResponse
import json
def json_to_obj():
    file_path = r"C:\Users\gersi\PycharmProjects\djangoProject\base\data.json"
    with open(file_path, "r") as f:
        data = json.load(f)

    return data

def format_comp_data(data):
    company_info = {}
    for comp in data:
        company_name = comp['job']['company']['name']
        revenue = comp['job']['company'].get('revenue', None)
        salary = comp['salary']
        if company_name not in company_info:
            company_info[company_name] = {'revenue': revenue,
                                          'salaries': [float(salary)], 'employee_count': 1}
        else:
            company_info[company_name]['salaries'].append(float(salary))
            company_info[company_name]['employee_count'] += 1
    for company_name, info in company_info.items():
        salaries = info['salaries']
        mean_salary = round(sum(salaries) / len(salaries), 2)
        info['mean_salary'] = mean_salary
        info['spendings'] = round(sum(salaries), 2)

    return company_info


def home(request):
    data = json_to_obj()
    company_names = format_comp_data(data)
    context = {
        "company_name": company_names,
    }
    # print(context['company_name'])
    return render(request, 'companies_view.html', context)


def comp_profile_info(employees):
    male = 0
    female = 0
    devided_by_age = {
        '0_28': {'count': 0, 'spendings': 0},
        '28_34': {'count': 0, 'spendings': 0},
        '34_40': {'count': 0, 'spendings': 0},
        '40_100': {'count': 0, 'spendings': 0},
    }
    total_spending = 0
    for rec in employees:
        age = rec['age']
        gender = rec['gender']
        salary = rec['salary']
        if gender == 'male':
            male += 1
        else:
            female += 1

        age_group = None
        if age > 0 and age <= 28:
            age_group = '0_28'
        elif age > 28 and age <= 34:
            age_group = '28_34'
        elif age > 34 and age <= 40:
            age_group = '34_40'
        elif age > 40 and age <= 100:
            age_group = '40_100'

        if age_group:
            devided_by_age[age_group]['count'] += 1
            devided_by_age[age_group]['spendings'] += float(salary)
            total_spending += float(salary)

    tot_emp = male+female
    male_perc = round((male*100) / tot_emp)
    female_perc = 100 - male_perc

    for age_group, info in devided_by_age.items():
        info['spendings'] = round(info['spendings'], 2)


    extra_info = {
        'male_perc':male_perc,
        'female_perc':female_perc,
        'age_group':devided_by_age,
        'tot_emp':tot_emp,
        'total_spending':round(total_spending,2)
    }
    return extra_info


def open_company_profile(request, pk):
    data = json_to_obj()
    company = format_comp_data(data)
    mean_salary = company[pk]['mean_salary']
    employees = [emp for emp in data if emp['job']['company']['name'] == pk]

    comp_profile = comp_profile_info(employees)


    context = {
        'company_name':pk,
        'employees':employees,
        'mean_salary':mean_salary,
        'comp_profile':comp_profile,
    }
    return render(request, 'company_profile.html', context)