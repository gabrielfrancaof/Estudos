//Escreva um programa que solicite ao usuario o salario atual e mostre o salário acrescido de 5% de comissão

package exercicios;

import java.util.Scanner;

public class exerc02 {
    static void main() {
        Scanner sc = new Scanner(System.in);
        System.out.print("Digite o seu salário atual: ");
        double salario = sc.nextInt();
        double comissao = salario+(salario*0.05);
        System.out.println("Seu salário com a comissão fica em: R$"+comissao);
    }
}
