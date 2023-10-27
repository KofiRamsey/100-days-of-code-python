print('Welcome to the Tip Calculator')

bill = float(input('What is the total bill? $'))
people = int(input('How many people are splitting the bill? '))
percentage = float(input('Tip percentage? 10, 12 or 15? ')) / 100

total_tip = bill * percentage
total_bill_with_tip = bill + total_tip
total_per_person = total_bill_with_tip / people

print(f'Each person will pay: ${total_per_person:.2f}')
