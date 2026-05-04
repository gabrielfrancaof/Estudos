package com.gabrielfranca.maratonajava.introducao;

//dado um determinado salario, qual a taxa de imposto que será pago

public class Aula05EstruturasCondicionais04 {
    static void main(String[] args) {
    double salarioAnual = 2000;
    double primeiraFaixa = 9.7 /100;
    double segundaFaixa = 37.35 /100;
    double terceiraFaixa = 49.5 /100;
    double valorDoImposto;


    if (salarioAnual <= 34712){
        valorDoImposto = salarioAnual*primeiraFaixa;
    } else if (salarioAnual >= 34713 && salarioAnual <= 68507) {
        valorDoImposto = salarioAnual*segundaFaixa;
    } else {
        valorDoImposto = salarioAnual*terceiraFaixa;
    }
        System.out.printf("O valor do imposto do salário anual de $%.2f, será: $%.2f",salarioAnual, valorDoImposto);
    }
}
