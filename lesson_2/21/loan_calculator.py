#definte all imports on the top but we will need none here

#define all global variables
input_type_prompt_dictionary = {
  loan_amount: "Please type in the loan amount in dollars and cents",
  monthly_interest_rate: "Please type in the loan amount in percentage",
  loan_duration: "Please type in the loan duration in months"
}

#define all functions
def ask_for_input(input_type):
  while true:
    value = input("Type in the f'{input_type_prompt_dictionary[input_type]}'")
    if validator(value, input_type):
      return float(value)
    else:
      print("Invalid input")

def validator(value, input_type):
  case input_type:
    when loan_amount:
      try:
        float(value)
        return float(value) > 0
      except ValueError:
        return False

    when monthly_interest_rate:
      try:
        float(value)
        return float(value) >= 0
      except ValueError:
        return False
    when loan_duration:
      try:
        float(value)
        return float(value) >= 0
      except ValueError:
        return False

#define the loop
while True:
  loan_amount = ask_for_input("loan amount")
  interest_rate = ask_for_input("interest rate")
  loan_duration = ask_for_input("loan duration")
  break

