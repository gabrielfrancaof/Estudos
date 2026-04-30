//Escreva um programa que solicite ao usuario a distância entre duas cidades e o tempo de viagem. O programa deverá calcular e exibir a velociade média de um carro que vai de uma cidade para outra usando a formula VM = distancia / tempo

package exercicios;
import java.util.Scanner;
public class exerc03 {
    static void main() {
        Scanner sc = new Scanner(System.in);
        System.out.print("Digite a distância entre as cidades: ");
        int distancia = sc.nextInt();
        System.out.print("Digite o tempo de viagem: ");
        int duracao = sc.nextInt();

        double velocidadeMedia = distancia/duracao;

        System.out.println("A velocidade média da viagem é: "+ velocidadeMedia+"km/h");
        sc.close();



    }
}
