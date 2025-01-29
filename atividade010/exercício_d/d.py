import os


from calcular_temp.convertertemp import converter_temp
from calcular_temp.convertertemp import fahrenheint

os.system('cls')

celsius = converter_temp(fahrenheint)
print(f'A temperatura {fahrenheint}°F em celsius é {celsius:.2f}°C.')