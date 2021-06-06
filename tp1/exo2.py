
seconds = int(input('Entrez le nombre de secondes: '))

hours, seconds =  divmod(seconds, 3600)

minutes, seconds = divmod(seconds, 60)

print(hours, 'h', minutes, 'm', seconds, 's')