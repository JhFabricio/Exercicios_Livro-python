#Enunciado: 1. Quantos segundos há em 42 minutos e 42 segundos?

#Variáveis
minutos = 42
segundos = 42

#Cálculos
minutos_convertidos = minutos * 60
total = minutos_convertidos + segundos

#Resposta final
print(f'{minutos} minutos e {segundos} segundos são equivalentes a {total} segundos')

#--/--/--/--

#Enunciado: 2. Quantas milhas há em 10 quilômetros? 
#Dica: uma milha equivale a 1,61 quilômetro.

#Variáveis
km = 10
milhas = round(km * 0.62137, 2)

#Resposta final
print(f'Há {milhas} milhas em {km} km')

#--/--/--/--

#Enunciado: 3. Se você correr 10 quilômetros em 42 minutos e 42 segundos, qual é o seu passo médio? Qual é a sua velocidade média em milhas por hora?

#Variáveis
km = 10
segundos = 2562

#Cálculos de conversão de km para milhas
milhas = round(km * 0.62137, 2)

#Cálculos de conversão de segundos para minutos e minutos para horas
minutos = segundos / 60
horas = minutos / 60

#Cálculo de velocidade média utilizando os valores que obtivemos
vm = round(milhas / horas, 2)

#Resposta final
print(f'Se você correr {km} km em {minutos} minutos a sua velocidade média é {vm} milhas por horas')

#--/--/--/--
