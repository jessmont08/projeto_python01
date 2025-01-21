import os


os.system('cls')

def converter_temp(fahrenheint):
    celsius = (fahrenheint - 32) * 5 / 9

    return celsius

fahrenheint = float(input('Digite a temp em °F: '))

celsius = converter_temp(fahrenheint)
print(f'A temperatura {fahrenheint}°F em celsius é {celsius}°.')