//Escreva um programa que calcule as duas raizes de uma equação de 2º Grau ax**2+bx+c. conhecendo os valores dos coeficientes da mesma. Suponha que as raizes são reais.

package exercicios;
import javax.imageio.ImageTranscoder;
import java.util.Scanner;
public class exerc04 {
    static void main() {
        Scanner sc = new Scanner(System.in);
        System.out.print("Digite o valor de a: ");
        int valorA = sc.nextInt();
        System.out.print("Digite o valor de b: ");
        int valorB = sc.nextInt();
        System.out.print("Digite o valor de c: ");
        int valorC = sc.nextInt();

        double delta = Math.pow(valorB, 2) - 4*valorA*valorC;

        double raizDelta = Math.sqrt(delta);

        double x1 = (-valorB + raizDelta)/(2*valorA);
        double x2 = (-valorB - raizDelta)/(2*valorA);

        System.out.println("O valor do x1 é: "+x1+" e o valor do x2 é: "+x2);
    }
}
