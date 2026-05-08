package com.gabrielfranca.maratonajava.introducao;

public class Aula07Arrays02 {
    static void main(String[] args) {
        // byte, short, int, long, flooat e double 0
        // char '\u0000' ' '
        // boolean false
        // String null

        String [] nomes = new String[3];
        nomes[0] = "Goku";
        nomes[1] = "Pikachu";
        nomes[2] = "Luffy";

        for (int i = 0; i < 3; i++) {
            System.out.println(nomes[i]);

        }

        /* Os arrays tem que ser mudado sempre o tamanho deles, mas existe uma opção de mudar automático no for:
        for (int i = 0; i < nomes.length; i++) {
            System.out.println(nomes[i]);
        }

        */
    }
}
