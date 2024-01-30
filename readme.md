
# Jogo de Combate em Python

Este projeto é um jogo de combate simples feito em Python. Ele demonstra o uso de vários conceitos de programação orientada a objetos (POO) e também utiliza uma biblioteca interna.


## Conceitos Abordados

1. **Classes e Objetos**: As classes são definidas usando a palavra-chave `class`. Um objeto é uma instância de uma classe. Neste projeto, temos três classes principais: `Personagem`, `Heroi` e `Inimigo`.

2. **Herança**: A herança é um conceito fundamental da POO que permite criar uma nova classe a partir de uma classe existente. Neste projeto, a classe `Heroi` e `Inimigo` herdam da classe `Personagem`.

3. **Encapsulamento**: O encapsulamento é o conceito de ocultar os detalhes internos de uma classe e permitir o acesso apenas através de métodos públicos. Neste projeto, os atributos `__nome`, `__vida`, `__nivel`, `__habilidade` e `__tipo` são privados e só podem ser acessados através de métodos getter.

4. **Polimorfismo**: O polimorfismo permite que um objeto seja tratado como uma instância de sua classe ou de qualquer classe de sua hierarquia. Neste projeto, o método `atacar` na classe `Personagem` é sobrescrito na classe `Heroi` para implementar um ataque especial.

5. **Bibliotecas**: Este projeto utiliza a biblioteca interna do Python chamada `random`. Essa biblioteca é usada para calcular de forma aleatória o dano causado quando o jogador faz um ataque.



## Instalação

1. Certifique-se de ter o Python instalado em seu sistema a partir da versão 3.11.5 64bit ou superior.
2. Clone esse repositório.
3. Abra seu terminal e navegue até o diretório onde o arquivo foi baixado.
4. Execute o arquivo: `jogo.py` no seu IDE ou Editor de código-fonte de sua preferência para iniciar o jogo.

    
## Estrutura do Jogo

- O jogo começa com a criação de uma instância da classe `Jogo`. A classe `Jogo` gerencia o jogo, criando instâncias das classes `Heroi` e `Inimigo` e gerenciando a lógica do jogo, como a batalha entre o herói e o inimigo.

- Durante a batalha, o usuário pode escolher entre atacar normalmente ou usar um ataque especial. Após cada turno, o inimigo também ataca o herói. O jogo continua até que o herói ou o inimigo tenham 0 de vida.



## Aprendizados

- A cada novo projeto proposto pela Rocketseat sempre há novos aprendizados e desafios, focados em nos levar a pensar fora da caixa e com isso sempre aprimorando cada vez mais o meu conhecimento adquirido em desenvolvimento FullStack.

- **Classes e Objetos**: Através deste projeto, pude reforçar minha compreensão sobre classes e objetos em Python. Aprendi a definir classes usando a palavra-chave `class` e a criar objetos dessas classes.

- **Herança**: Aprendi a criar subclasses que herdam de uma classe base. Isso permitiu que eu reutilizasse código e mantivesse a organização do código limpa e eficiente.

- **Encapsulamento**: Entendi a importância do encapsulamento ao ocultar os detalhes internos de uma classe e permitir o acesso apenas através de métodos públicos. Isso ajuda a manter a integridade dos dados e a prevenir erros.

- **Polimorfismo**: Aprendi a usar o polimorfismo para permitir que um objeto seja tratado como uma instância de sua classe ou de qualquer classe de sua hierarquia. Isso aumentou a flexibilidade do código.

- **Bibliotecas**: Aprendi a usar a biblioteca interna do Python chamada `random` para gerar números aleatórios. Isso foi útil para adicionar um elemento de aleatoriedade ao jogo. Assim como aprendi a fazer uso de bibliotecas de terceiros.

