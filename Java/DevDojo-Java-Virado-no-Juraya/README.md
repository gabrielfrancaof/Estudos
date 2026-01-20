# ☕ Maratona Java virado no Jiraya - DevDojo

Aqui insiro todos os conhecimentos adquiridos ao longo do curso desenvolvido pelo [DevDojo](https://www.youtube.com/@DevDojoBrasil).

## 💻 Resumos das aulas

| Módulo | Status | O que pratiquei |
| :--- | :--- | :--- |
| 01 - Introdução | 🟢 Concluído | Instalar IDE e pacote JDK, organização de pacotes e comentários|
| 02 - Tipos Primitivos | 🟢 Andamento | Conheci os 8 tipos primitivos e fiz um exercício com variáveis|
| 03 - Operadores | 🟡 A fazer | - |
| 04 - Estruturas condicionais | 🔴 A fazer | - |
| 05 - Estruturas de Repetição | 🔴 A fazer | - |
| 06 - Arrays | 🔴 A fazer | - |
| 07 - Orientação de Objetos | 🔴 A fazer | - |
| 08 - Exceções | 🔴 A fazer | - |


## 01 - Introdução

### **Aula 05 - Executando o codigo manualmente**
- Nomes de classes sempre tem a primeira letra maiuscula, se for palavra composta, colocar a primeira letra de cada maiuscula, exemplo: OlaDevDojo
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
- Temos 8 tipos de primitivos, sendo eles: int, double, flooat, char, byte, short, long, boolean.
- psvm ou main + tab --> Escreve o código "static void main()"
- Variáveis são espaço na memória.
- Na criação de variável, a primeira letra tem que ser minúscula, se for mais de uma palavra, as outras devem ser maiúsculas, ex: int idadeDoPaiNaHoraDoCadastro
- Para adicionar texto na hora de imprimir, basta colocar ""+ dentro da linha de comando, exemplo: System.out.println("A idade é "+age);
- Atalho para o println --> sout

### **Aula 11 - Declaração e tamanho em memória**
- Todos os tipos primitivos são númericos, exceto boolean, a diferença é a quantidade de valor que podem ser colocados nas variáveis
- Ctrl + D duplica linha de código

### **Aula 12 - Casting**
- É forçar um valor dentro de uma vaiável que não cabe dentro de outra, ex: colocar um número double dentro do float.
- Casting não é uma boa prática, o ideal é trocar o tipo da variável.

### **Aula 13 - Strings**
- A string não é um tipo primitivo, é uma classe, e como toda classe, deve ser escrita com letra maiúscula, ex:
```Java
Sting = nome "Gabriel";
```

### **Aula 14 - Exercício**
- Foi feito um exercício para escrever uma frase usando variáveis e contatenar no final

## 03 - **Operadores**

### **Aula 15 - Aritiméticos**
