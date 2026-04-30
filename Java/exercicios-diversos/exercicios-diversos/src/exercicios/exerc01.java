//#Desenvolva um programa que solicite ao usario os valores dos lados de um retângulo e calcule e mostre seu perímetro e sua área
package exercicios;

import java.util.Scanner;

public class exerc01 {
    static void main() {
        Scanner sc = new Scanner(System.in);
        System.out.print("Digite o primeiro lado: ");
        int lado1 = sc.nextInt();
        System.out.print("Digite o segundo lado: ");
        int lado2 = sc.nextInt();
        int calculoArea = lado1*lado2;
        int calculoPerimetro = 2*(lado1+lado2);

        System.out.println("A área do seu retângulo é: " + calculoArea + " e o perimetro é: "+ calculoPerimetro);
        sc.close();
    }

}
