import profile_planner.Profile as Profile
import profile_planner.Salary as Salary
import profile_planner.Utils as Utils
import json


period = {'duration': 10,
          'pay_debts': [],
          'default_invest': 'IBKR',
          'severance_plan': {'pension_rewards': 'pension',
                             'above_pension_rewards': 'gemel_rewards',
                             'above_pension_compensation': 'gemel_compensation'}
          }

user = ''
expenses = 6000

with open('../database/'+user+'_salary.json') as f:
    salary_args = json.load(f)
with open('../database/'+user+'_assets.json') as f:
    assets_args = json.load(f)

salary = Salary.Salary(**salary_args)
print(salary.net)
print(salary.taxable_gross)
print(salary.severances)

profile = Profile.Profile()
for asset in assets_args.keys():
    profile.add_asset(asset, assets_args[asset])

# Profile.add_asset(asset)
plan = [period]

money_pool = 0
for period in plan:
    for month in range(period['duration']):
        money_pool += salary.net
        for severance in period['severance_plan'].keys():
            profile.invest_asset(period['severance_plan'][severance], salary.severances[severance])
        money_pool += profile.progress_month()
        # print(money_pool)
        # print(profile.assets['IBKR'].value)

        # pay_debts = period['pay_debts']
        # for debt in pay_debts.keys():
        #     Profile.pay_debt(debt,pay_debts[debt])
        #
        # Profile.invest_asset(period['default_invest'], money_pool)