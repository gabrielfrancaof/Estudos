# ☕ Maratona Java virado no Jiraya - DevDojo

Aqui insiro todos os conhecimentos adquiridos ao longo do curso desenvolvido pelo [DevDojo](https://www.youtube.com/@DevDojoBrasil).

## 💻 Resumos das aulas

| Módulo | Status | O que pratiquei |
| :--- | :--- | :--- |
| 01 - Introdução | 🟢 Concluído | Instalar IDE e pacote JDK, organização de pacotes e comentários|
| 02 - Tipos Primitivos | 🟢 Concluído | Conheci os 8 tipos primitivos e fiz um exercício com variáveis|
| 03 - Operadores | 🟢 Concluído | Quais são os operadores,como fazer operações dentro de variáveis e do print e quais são os operadores lógicos |
| 04 - Estruturas condicionais | 🟡 Andamento | - |
| 05 - Estruturas de Repetição | 🔴 A fazer | - |
| 06 - Arrays | 🔴 A fazer | - |
| 07 - Orientação de Objetos | 🔴 A fazer | - |
| 08 - Exceções | 🔴 A fazer | - |


## 01 - Introdução

### **Aula 05 - Executando o codigo manualmente**
- Nomes de classes sempre tem a primeira letra maiuscula, se for palavra composta, colocar a primeira letra de cada maiuscula, exemplo: `OlaDevDojo`
```java
public class OlaDevDojo {
    public static void main (String[] args) {
            System.out.println("Hello world!");
    }
}
```
- O nome da classe publica **DEVE** ter o mesmo nome do arquivo.
- O " ; "serve para informar que aquela linha de código terminou.
- O arquivo .java é o arquivo de linguagem, o arquivo .class é o arquivo em bytecode, ou seja, linguagem de máquina.

### **Aula 08 - Organizando o código em pacotes**
- O Java deve ser organizado em pacotes, principalmente em projetos grandes que irão ter muitas classes.
- Os pacotes ajudam a organizar e agrupar as classes que possuem coisas em comum.
- O nome do pacote deve ser a url do seu site, porém, invertida ex: o site é tatamulambo.com.br, a pasta se torna br.com.tatamulambo.(aqui vem o nome do projeto).

### **Aula 09 - Comentários**
- Existem 3 tipos de comentários:
    ```java
    Em linha: //
    Multiplas linhas: /*   */
    Javadoc: /**
    ```

- Quanto menos comentários melhor, pois se estiver usando muitos, significa que seu código não está limpo.
- Comentários podem gerar erros, pois quando o código for atualizado, muitas as vezes os comentários não são atualizados junto, então podem induzir ao erro.

## 02 - Tipos primitivos

### **Aula 10 - Convenções de variáveis**
- Temos 8 tipos de primitivos, sendo eles: `int, double, flooat, char, byte, short, long, boolean.`
- `psvm` ou `main` + tab --> Escreve o código `static void main()`
- Variáveis são espaço na memória.
- Na criação de variável, a primeira letra tem que ser minúscula, se for mais de uma palavra, as outras devem ser maiúsculas, ex: `int idadeDoPaiNaHoraDoCadastro`
- Para adicionar texto na hora de imprimir, basta colocar ""+ dentro da linha de comando, exemplo: `System.out.println("A idade é "+age);`
- Atalho para o println --> sout

### **Aula 11 - Declaração e tamanho em memória**
- Todos os tipos primitivos são numéricos, exceto boolean, a diferença é a quantidade de valor que podem ser colocados nas variáveis
- Ctrl + D duplica linha de código

### **Aula 12 - Casting**
- É forçar um valor dentro de uma variável que não cabe dentro de outra, ex: colocar um número double dentro do float.
- Casting não é uma boa prática, o ideal é trocar o tipo da variável.

### **Aula 13 - Strings**
- A string não é um tipo primitivo, é uma classe, e como toda classe, deve ser escrita com letra maiúscula, ex:
```Java
Sting = nome "Gabriel";
```

### **Aula 14 - Exercício**
- Foi feito um exercício para escrever uma frase usando variáveis e concatenar no final

## **03 - Operadores**

### **Aula 15 - Aritiméticos**
- A operação aritimética, pode ser feita no println, porém, a ordem irá influenciar se irá somar ou concatenar, ex: (10+10) -> irá somar, ("valor"+10+10) -> irá concatenar e (10+10+"valor") -> irá somar e depois concatenar
- Nas operações deve-se tomar cuidado com os tipos da variavel, por exemplo, ao dividir dois números INT o resultado será um número inteito, ex 20/10=0, para isso, devera usar um número double por exemplo para ter o resultado esperado 20/10=0,5 (int/double)

### **Aula 16 - Relacionais**
- Para calcular o resto, é utilizado o sinal de `%`
- Os operadores lógicos são utilizados pelos simbolos `< > <= >= ==  !=`
- O resultado dos operadores lógicos irão sempre retornar booleanos, ex: 10 > 20 ---> False

### **Aula 17, 18 e 19 - Lógicos AND, OR e Atribuição**
- Para usar o AND é utilizado `&&`
- Para usar o OR é utilizado `||`
- Para atribuições, itilizar `+= -= *= /= %= ++ --`

## **04 - Estruturas Condicionais**

### **Aula 20, 21 - IF, ELSE, ELSE IF**

### **Aula 22 - Operador ternário**

- O operador ternário em Java (? :) é uma expressão condicional que retorna um valor, não sendo estritamente uma string ou uma variável. Ele funciona como um if-else simplificado em uma única linha, onde o resultado final geralmente é atribuído a uma variável de qualquer tipo

- Sua definição é: `(condição) ? valor_se_verdadeiro : valor_se_falso;`

Exemplo:

```java
        double salario = 5000;
        String mensagemDoar = "Eu vou doar 500 pro DevDojo";
        String mensagemNaoDoar = "Eu ainda não tenho condições, mas vou ter";
        String resultado;
        if (salario > 5000){
            resultado = mensagemDoar;
        }else {
            resultado = mensagemNaoDoar;
        }
        System.out.println(resultado);
```
Em vez de colocar um If-else, ele pode ser escrito da seguinte forma:

```java
        double salario = 6000;
        String mensagemDoar = "Eu vou doar 500 pro DevDojo";
        String mensagemNaoDoar = "Eu ainda não tenho condições, mas vou ter";
        String resultado = (salario > 5000) ? mensagemDoar : mensagemNaoDoar;
        System.out.println(resultado);
```
E ainda é possível simplificar mais

```Java
        double salario = 6000;
        String resultado = (salario > 5000) ? "Eu vou doar 500 pro DevDojo" : "Eu ainda não tenho condições, mas vou ter";
        System.out.println(resultado);
```

### **Aula 25 - Switch**
- Os valores que podem ser utilizados no `switch` são: char, int, byte, short, enum, String
- O switch é usado no lugar de If Else em alguns casos para simplificar o código, por exemplo, em vez de usar o if para cada dia da semana é possível usar o Switch:
```Java
byte dia = 1;
switch (dia){
    case 1:
        System.out.println("Domingo");
        break;
```
(Nesse exemplo ele identifica valor da variável, e caso seja igual ao solicitado ele irá imprimir)
- É muito importante usar o `break`, pois ele também irá executar os próximos `case` se existirem
- Também é importante usar o `default` por uma questão humana, caso tenha alguma opção que não tenha no case, ele irá retornar o que pedir, por exemplo:

```Java
byte dia = 35;
switch (dia){
    case 1:
        System.out.println("Domingo");
        break;
    default:
        System.out.println("Opção inválida");
        break;
```

## **05 - Estruturas de repetição**
### **Aula 27 - Laços de repetição while, do while, for**
- `while` precisa sempre retornar um valor booleano e:
```java
int count = 0;
        while (count < 10){
            System.out.println(count);
            count += 1;
```
- o `do` ele é executado uma vez independente se ser verdadeiro ou não
- o `for` é feito da seguinte forma: `for (;;)`, funcionando assim -> `for ( variavel ; comparação ; como a variavel vai alterar o status)`. Exemplo:
```java
for (int i = 0; i<10; i++){
                System.out.println("For "+i);
```

