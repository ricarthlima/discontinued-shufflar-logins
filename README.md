# Programa para sortear logins-monitores
Utilizado pelos monitores da cadeira de Programação 01 para sortear qual monitor corrigirá a lista de qual aluno de modo a impedir/retardar repetições no limite do possível, e o fazê-lo de forma justa. É importante dizer que um "resto" sempre será gerado quando o número de alunos não for dividendo do número de monitores, esses casos deverão ser resolvidos socialmente e não serão registrados.

## Instruções
O arquivo main.py contém o código. Ele depende dos arquivos monitores.txt e logins.txt.

### monitores.txt
Este arquivo deverá seguir a estrutura de um monitor por linha. O nome do monitor virá como a primeira palavra da linha (separada por espaços), daí em diante todas as palavras serão logins que fazem parte do histórico do monitor (ou seja, alunos que ele já corrigiu a lista no passado). Esse arquivo pode mudar dependendo da disponibilidade dos monitores.

### logins.txt
Este arquivo terá uma lista de logins (separados por quebras de linha) onde cada login é um aluno que enviou os arquivos da lista em questão. Lembrando que esse arquivo não é fixo, pois por vezes os alunos deixam de enviar.

### lista.txt
O programa pode gerar um arquivo extra que guarda as informações sobre as designações da lista atual.

## Melhorias propostas
- Fazer com que o programa reconheça quando não é mais possível não repetir um aluno para os monitores e passe a lidar com isso com distância para repetição.
- Lidar com o problema do resto de forma mais eficiente, automatizada e justa.

## Autor
**Ricarth Lima** (rrsl@cin.ufpe.br)
