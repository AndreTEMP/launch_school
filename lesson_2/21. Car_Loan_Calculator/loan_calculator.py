#definte all imports on the top but we will need none here

#define all global variables
input_type_prompt_dictionary = {
  'loan_amount': 'Please type in the loan amount in dollars and cents (Must be greater than 0)',
  'annual_percentage_rate': 'Please type in the annual percentage rate in percentage (Must be greater than 0)',
  'loan_duration': 'Please type in the loan duration in years (Must be greater than 0)'
}

#define all functions
def input_prompt(input_type):
  return f'Type in the {input_type_prompt_dictionary[input_type]} \n'

def results_prompt(monthly_interest_rate):
  return f'Your your monthly payment is ${monthly_interest_rate:.2f} \n'


def redo_prompt():
  return 'Would you like to run the calculator again? \n'

def ask_for_input(input_type):
  while True:
    prompt = input_prompt(input_type)
    value = input(prompt)
    valid, value = validate_and_process_values(value, input_type)
    if valid:
      return value
    else:
      print('Invalid input. Please insert a positive number')

def validate_and_process_values(value, input_type):
  '''
  Process the value and return a tuple of a boolean and the value
  '''
  match input_type:
    case 'loan_amount':
      try:
        #unsure of something here
        value = float(value)
        return (float(value) > 0, value)
      except ValueError:
        return (False, 0)

    case 'annual_percentage_rate':
      try:
        value = float(value)
        return (float(value) > 0, (value / 100) / 12)
      except ValueError:
        return (False, 0)
    case 'loan_duration':
      try:
        value = float(value)
        return (float(value) > 0, value * 12)
      except ValueError:
        return (False, 0)

#define the loop
while True:
  loan_amount = ask_for_input('loan_amount')
  monthly_interest_rate = ask_for_input('annual_percentage_rate')
  loan_duration_in_months = ask_for_input('loan_duration')

  monthly_payment = loan_amount * (monthly_interest_rate / (1 - (1 + monthly_interest_rate) ** (-loan_duration_in_months)))
  print(results_prompt(monthly_payment))
  redo_input = input(redo_prompt())
  if redo_input != 'yes':
    continue
  else:
    break
