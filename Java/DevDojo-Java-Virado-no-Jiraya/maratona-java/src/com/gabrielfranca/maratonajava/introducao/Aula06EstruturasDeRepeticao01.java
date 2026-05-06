package com.gabrielfranca.maratonajava.introducao;

public class Aula06EstruturasDeRepeticao01 {
    static void main(String[] args) {
        // whille, do whille, for

        int count = 12;
        while (count < 10){
            System.out.println(count);
            count += 1;
        }
        do {
            System.out.println("Dentro do do-while");
        }
            while (count < 10);

            for (int i = 0; i<10;i++){
                System.out.println("For "+i);
            }
    }
}