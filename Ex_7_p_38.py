S=str(input('introduceti sirul:'))
#a)numarul de aparitii a caracterului 'A' in sirul S:
print('a)numarul de aparitii a caracterului A: ',S.count('A'))
#b)sirul obtinut prin substituirea caracterulu 'A' prin cracterul '*':
print('b)sirul obtinut prin substituirea caracterulu A prin cracterul * :',S.replace('A','*'))
#c)sirul obtinut prin radierea din sirul S a tuturor aparitiilor caracterului 'B':
print('c)sirul obtinut prin radierea caracterului B:',S.replace('B',''))
#d)numarul de aparitii ale silabei 'MA' in sirul S:
print("d)numarul de aparitii a caracterului 'MA': ",S.count('MA'))
#e)sirul obtinut prin substituirea tuturor aparitiilor in sirul S a silabei 'MA' prin silaba 'TA':
print('e)sirul obtinut prin substituirea silabei MA prin TA:',S.replace('MA','TA'))
#f)sirul obtinut prin radierea din sirul S a tuturor aparitiilor silabei 'TO'
print('c)sirul obtinut prin radierea silabei TO:',S.replace('TO',''))
#g)scrierea inversa a sirului S
print('g)sirul scris invers:',S[::-1])