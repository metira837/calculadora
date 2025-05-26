import random

fruta = ['maça', 'banana', 'uva', 'melancia']
palavra_escolhida = random.choice(fruta)
print(palavra_escolhida)
print('tente adivinhar a palavra, vocé terá três tentativas \n(uma dica: a palavra é uma fruta)')
palavra_do_usuario = []
tentativa = 3

while True:
   escolha = input('digite uma letra:\n')
   if escolha in palavra_escolhida:  
      print('acertou')
      palavra_do_usuario.append(escolha)
   else:
      tentativa -= 1
      print(f'vocé errou, voce agora tem {tentativa}')
   if tentativa <= 0:
      print('vocé perdeu')
      break
   if ''.join(sorted(palavra_do_usuario)) == ''.join(sorted(palavra_escolhida)):
         print('parabens, vocé ganhou')
         continue
print(f'a palavra era {palavra_escolhida}')