package com.gabrielfranca.maratonajava.introducao;

public class Aula06EstruturasDeRepeticao04 {
    // Dado o valor de um carro, descubra em quantas vezes ele pode ser parcelado
    // Condição valorParcela >=1000
    static void main(String[] args) {

        double valorCarro = 10000;
        /* Uma das formas de fazer é assim:
        for (int parcela = 1; parcela <=valorCarro ; parcela++) {
            double valorParcela = valorCarro/parcela;
            if (valorParcela >= 1000){
                System.out.println("Parcela "+ parcela+ "R$"+valorParcela);
            }else {
                break;
            }
        }
        Porém dá para economizar linhas
         */
        for (int parcela = 1; parcela <= valorCarro ; parcela++) {
            double valorParcela = valorCarro/parcela;
            if (valorParcela < 1000){
                break;
            }
            System.out.println("Parcela "+ parcela+ "R$ "+valorParcela);

        }



    }
}
