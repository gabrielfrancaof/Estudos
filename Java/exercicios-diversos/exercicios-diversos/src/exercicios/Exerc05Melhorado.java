//Neste exercicio usei o gemini para me dar algumas dicas de como melhorar o meu código, li da primeira vez que ele formou e fiz seguindo em base o que consgui absorver lendo.

package exercicios;

import java.util.Scanner;

public class Exerc05Melhorado {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.print("Digite o seu peso em kg: ");
        double peso = sc.nextDouble();
        System.out.print("Digite a sua altura em cm (ex: 172): ");
        int altura = sc.nextInt();
        System.out.print("Digite a sua idade: ");
        int idade = sc.nextInt();
        System.out.print("Digite o seu sexo (M/F): ");
        String sexo = sc.next();
        System.out.print("Digite o seu nível de atividade física (Sedentario, leve, moderado ou ativo): ");
        String atividade = sc.next();

        double tmb = 0;

        if (sexo.equalsIgnoreCase("m")) {
            tmb = (66.5 + (13.75 * peso) + (5 * altura) - (6.75 * idade));
        } else if (sexo.equalsIgnoreCase("f")) {
            tmb = (665.1 + (9.56 * peso) + (1.85 * altura) - (4.67 * idade));
        } else {
            System.out.println("Sexo inválido!");
        }

        // No if de cima não preciso usar novamente o "double", pois o valor do tmb já foi definido como "double" acima

/*      // fiz desta forma mas ainda ficou errado pois usei muito print repetidos
        if (tmb > 0) {      //colocando desta forma evita erros no código
            if (atividade.equalsIgnoreCase("sedentario")) {
                double sedentario = tmb * 1.2;
                System.out.printf("A sua taxa metabólica basal é: %.2f\n", sedentario);
            } else if (atividade.equalsIgnoreCase("leve")) {
                double leve = tmb * 1.375;
                System.out.printf("A sua taxa metabólica basal é: %.2f\n", leve);
            } else if (atividade.equalsIgnoreCase("moderado")) {
                double moderado = tmb * 1.55;
                System.out.printf("A sua taxa metabólica basal é: %.2f\n", moderado);
            } else if (atividade.equalsIgnoreCase("ativo")){
                double ativo = tmb * 1.725;
                System.out.printf("A sua taxa metabólica basal é: %.2f\n", ativo);
            }else {
                System.out.println("Nível de atividade inválido"); //evita quebrar o código
            }
        }
*/
        if (tmb > 0) {
            double gastoTotal = 0;
            if (atividade.equalsIgnoreCase("sedentario")) {
                gastoTotal = tmb * 1.2;
            } else if (atividade.equalsIgnoreCase("leve")) {
                gastoTotal = tmb * 1.375;
            } else if (atividade.equalsIgnoreCase("moderado")) {
                gastoTotal = tmb * 1.55;
            } else if (atividade.equalsIgnoreCase("ativo")){
                gastoTotal = tmb * 1.725;
            }else {
                System.out.println("Nível de atividade inválido");
            }
            if (gastoTotal > 0){                         //Fazendo desta forma, eu reduzi varios print desnecessários e usei apenas um printf
                System.out.printf("A sua taxa metabólica basal é: %.2f\n", gastoTotal);
        }

        }
        sc.close();


    }
}
