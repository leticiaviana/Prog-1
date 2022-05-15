
from perguntas import quiz 
import json

def check_ans(difficult, question, ans, attempts, score):
    if question['answer'].lower() == ans.lower() and difficult == 'facil':
        print(f"Resposta certa! \nSua pontuação é {score + 1}!")
        return True
    elif question['answer'].lower() == ans.lower() and difficult == 'medio':
        print(f"Resposta certa! \nSua pontuação é {score + 2}!")
        return True
    elif question['answer'].lower() == ans.lower() and difficult == 'dificil':
        print(f"Resposta certa! \nSua pontuação é {score + 3}!")
        return True
    else:
        print(f"Resposta errada \nVocê tem {attempts - 1} tentativas! \nTente novamente...")
        return False


def intro_message():
    """
   Apresenta o usuário ao questionário e às regras e recebe uma entrada do cliente para iniciar o questionário.
    Retorna verdadeiro independentemente de qualquer tecla pressionada.
    """
    print("======== Está pronto para testar seus conhecimentos sobre computação? ========")
    print("São 8 perguntas, você pode pular qualquer uma delas digitando 'skip' a qualquer momento")
    input("\n\n____________Pressione qualquer tecla para começar!____________")
    return True


intro = intro_message()
jogador = str(input("\nDigite o nome do jogador: "))
difficult= int(input("\n\nEscolha a dificuldade:\n\n 1-FACIL\n\n 2-MÉDIO\n\n 3-DIFICIL\n"))
if difficult > 3 or difficult == 0:
    print("Escolha uma dificuldade válida")
elif difficult == 1:
    difficult = 'facil'
elif difficult == 2: 
    difficult = 'medio'
elif difficult == 3:
    difficult = 'dificil'

while True:
    score = 0
    for question in quiz[difficult]:
        attempts = 3
        while attempts > 0:
            print(question['question'])
            answer = input("Digite a alternativa e pressione ENTER (para pular a questão, digite 'skip') : ")
            if answer == "skip":
                break
            check = check_ans(difficult, question, answer, attempts, score)
            if check:
                if difficult == 'facil':
                    score += 1
                elif difficult == 'medio':
                    score += 2
                elif difficult == 'dificil':
                    score += 3
                break
            attempts -= 1

    break
print(f"\n\nSua pontuação final é {score}!\n\n Obrigada por jogar!\n\n")

# [ ] Ler o arquivo players.json
# [ ] Adicionar o jogar na lista com a pontuação
# [ ] Escreve o arquivo de novo

jogadores = None

with open('players.json', 'r') as f:
    jogadores = json.load(f)

jogadores.append({
    'nome': jogador,
    'pontuacao': score,
})

with open('players.json','w') as f:
    json.dump(jogadores, f)

print('===RANKING===\n')

for jogador_dict in jogadores:
    print(f'{jogador_dict["nome"]} - {jogador_dict["pontuacao"]}')