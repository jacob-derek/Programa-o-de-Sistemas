#converter input de Celcius pra Fahrenheit
#converter vai ser tipo output_F = 9/5 * input_Celcius + 32

user_Celcius = float(input("Quantos graus faz onde você mora?: "))
Celcius_to_Fahrenheit = ((9/5) * user_Celcius) + 32

print(f"Após uma conversão, sua temperatura equivale à {Celcius_to_Fahrenheit:.1f}°F")
