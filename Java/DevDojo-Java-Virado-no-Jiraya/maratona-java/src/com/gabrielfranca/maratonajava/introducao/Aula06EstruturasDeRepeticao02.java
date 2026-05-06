package com.gabrielfranca.maratonajava.introducao;

public class Aula06EstruturasDeRepeticao02 {
    static void main(String[] args) {
        //Imprima todos os números pares de 0 até 100000
        /*
        int num = 0;
        while (num < 100000){
            num += 2;
            System.out.println(num);
        }
         Fiz desta forma, mas também poderia ser feito com for e if */
        for (int i = 0; i < 100000; i++) {
            if (i % 2 == 0){
                System.out.println(i);
            }

        }

    }
}
