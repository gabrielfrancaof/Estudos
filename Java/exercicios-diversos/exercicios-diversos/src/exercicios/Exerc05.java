//Crie uma calculadora de taxa metabolica basal

package exercicios;
import java.util.Scanner;
public class Exerc05 {
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

        if (sexo.equalsIgnoreCase("m")) {
            double tmbM = (66.5 + (13.75*peso)+(5*altura)-(6.75*idade));
            if(atividade.equalsIgnoreCase("sedentario")){
                double sedentario = tmbM*1.2;
                System.out.printf("A sua taxa metabólica basal é: %.2f\n",sedentario);
            } else if (atividade.equalsIgnoreCase("leve")) {
                double leve = tmbM*1.375;
                System.out.printf("A sua taxa metabólica basal é: %.2f\n",leve);
            }else if (atividade.equalsIgnoreCase("moderado")) {
                double moderado = tmbM*1.55;
                System.out.printf("A sua taxa metabólica basal é: %.2f\n",moderado);
            }else {
                double ativo = tmbM*1.725;
                System.out.printf("A sua taxa metabólica basal é: %.2f\n",ativo);
            }
        }else if (sexo.equalsIgnoreCase("F")) {
            double tmbF = (665.1 + (9.56 * peso) + (1.85 * altura) - (4.67 * idade));
            if(atividade.equalsIgnoreCase("sedentario")){
                double sedentario = tmbF*1.2;
                System.out.printf("A sua taxa metabólica basal é: %.2f\n",sedentario);
            } else if (atividade.equalsIgnoreCase("leve")) {
                double leve = tmbF*1.375;
                System.out.printf("A sua taxa metabólica basal é: %.2f\n",leve);
            }else if (atividade.equalsIgnoreCase("moderado")) {
                double moderado = tmbF*1.55;
                System.out.printf("A sua taxa metabólica basal é: %.2f\n",moderado);
            }else {
                double ativo = tmbF*1.725;
                System.out.printf("A sua taxa metabólica basal é: %.2f\n",ativo);
            }
        } else {
            System.out.println("Sexo inválido!");
        }

        sc.close();
        }
    }
