# Programação Orientada a Objetos - Trabalho do Grau B

## Simulador de Execução de Processos

**Descrição:**  
O problema proposto é uma simulação de execução de um _pool_ de processos. O _pool_ consiste em uma fila de processos que é gerenciada pelo usuário. O usuário incrementa essa fila e decide em que momento os processos serão executados.

Os processos serão inseridos pelo usuário um a um e sempre no final da fila (portanto, na próxima posição livre do array). Os processos também devem ser executados na ordem em que foram inseridos na fila, a menos que o usuário solicite um processo específico pelo seu _pid_ (process identifier). Neste caso, um processo pode ser executado antes que o primeiro da fila. Quando isso acontece, os demais processos, sucessores do escolhido, devem “andar” uma posição à frente no array.

### Tipos de Processos
Existem quatro tipos específicos de processos. Cada tipo implementa um algoritmo para execução:
- **Processo de cálculo (_ComputingProcess_):** Executa o cálculo de uma expressão e imprime o resultado. Uma expressão é formada por dois operandos e uma operação (_+_, _-_, _*_ ou _/_).
- **Processo de gravação (_WritingProcess_):** Grava uma expressão em um arquivo chamado `computation.txt` sem sobrescrever registros já existentes.
- **Processo de leitura (_ReadingProcess_):** Lê o arquivo `computation.txt`, cria objetos do tipo _ComputingProcess_ e adiciona-os na lista de processos do sistema. Após a leitura, o arquivo deve ser “limpo”.
- **Processo de impressão (_PrintingProcess_):** Imprime na tela o _pool_ de processos, exibindo o _pid_, o tipo de processo e os atributos relacionados.

### Ações do Sistema
1. **Criar processo:** Cria um processo de um dos quatro tipos específicos e adiciona-o no final da fila.
2. **Executar próximo:** Executa o próximo processo da fila, removendo-o após a execução e atualizando a fila.
3. **Executar processo específico:** Solicita o _pid_ de um processo e o executa, mesmo que não seja o primeiro da fila. Após a execução, os sucessores ocupam uma posição à frente no array.
4. **Salvar a fila de processos:** Salva o estado atual da fila em um arquivo.
5. **Carregar do arquivo a fila de processos:** Inicializa o sistema com um array de processos do arquivo.

### Especificações e Restrições
- O array tem tamanho máximo de 100 elementos.
- A fila não deve conter “buracos”. Processos sucessores devem ser movidos uma posição à frente ao remover um processo.
- Sugestões:
  - Adicione um parâmetro ao construtor de _ComputingProcess_ para receber a expressão como string e quebrá-la em operandos e operador.
  - Passe a fila de processos como parâmetro nos construtores de _ReadingProcess_ e _PrintingProcess_.

### Entrega e Apresentação
- **Data:** Até as 19h do dia 21/11/2024, via Moodle.
- **Arquivos:** Projeto completo, modelagem e README em um único ZIP.
- **Apresentação:** No mesmo dia, em aula. O tempo e ordem serão definidos previamente.

### Avaliação
Critérios:
- Modelagem: 1.0 ponto.
- Classe _Process_ e subclasses: 3.0 pontos.
- Salvar e recuperar dados de arquivos: 2.0 pontos.
- Classe _Sistema_: 4.0 pontos, divididos entre:
  - Criar processo: 1.0 ponto.
  - Executar próximo: 1.0 ponto.
  - Executar processo específico: 1.0 ponto.
  - Funcionalidades gerais: 1.0 ponto.
- Comentários: Penalidade de 1.0 ponto por classe não comentada.

### Dicas
- Faça algo simples, mas funcional.
- Teste cada classe conforme for implementada.
- Planeje antes de começar.
- Não adicione regras não especificadas.
- Divida o trabalho ao longo do tempo.
- Trabalhos copiados ou feitos por terceiros serão penalizados.

**Boa sorte e bom trabalho!**

*Créditos: descrição baseada no trabalho original do Prof. Márcio Garcia Martins (Unisinos).*
