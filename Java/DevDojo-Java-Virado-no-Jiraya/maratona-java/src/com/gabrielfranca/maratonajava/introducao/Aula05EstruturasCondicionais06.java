package com.gabrielfranca.maratonajava.introducao;

public class Aula05EstruturasCondicionais06 {
    static void main(String[] args) {
        //Dados os valores de 1 a 7, imprima se é dia útil ou final de semana
        //Considerando 1 como domingo

        byte dia = 5;
        /* // inicialmente fiz desta forma, mas possui um jeito ainda mais fácil
        switch (dia){
            case 1:
                System.out.println("Dia de final de semana");
                break;
            case 2:
                System.out.println("Dia útil");
                break;
            case 3:
                System.out.println("Dia útil");
                break;
            case 4:
                System.out.println("Dia útil");
                break;
            case 5:
                System.out.println("Dia útil");
                break;
            case 6:
                System.out.println("Dia útil");
                break;
            case 7:
                System.out.println("Dia de final de semana");
                break;
            default:
                System.out.println("Opção inválida");
                break;
        }
        */
        switch (dia){
            case 1:
            case 7:
                System.out.println("Final de semana!");
                break;
            case 2:
            case 3:
            case 4:
            case 5:
            case 6:
                System.out.println("Dia útil!");
                break;
            default:
                System.out.println("Opção inválida!");
                break;
        }

    }
}
