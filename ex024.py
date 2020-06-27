cidade = str(input('Digite o nome da sua cidade: ')).strip()
split = cidade[:5].upper().split()
santo = 'SANTO' in split[0]
print(santo)
