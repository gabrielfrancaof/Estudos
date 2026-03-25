package com.gabrielfranca.maratonajava.introducao;

public class Aula05EstruturasCondicionais03 {
    public static void main(String[] args) {
        double salario = 6000;
        String mensagemDoar = "Eu vou doar 500 pro DevDojo";
        String mensagemNaoDoar = "Eu ainda não tenho condições, mas vou ter";
        //sem o Operador ternario seria essa string -> String resultado;
/*
        // até poderia fazer dessa forma, mas o melhor é usar várias variáveis de uma só vez
        if (salario >= 5000)
            System.out.println(mensagemDoar);
        else System.out.println( mensagemNaoDoar);
*/
/*
        //dessa forma também é possivel, porém com o operador ternario, utiliza-se apenas uma linha
        if (salario > 5000){
            resultado = mensagemDoar;
        }else {
            resultado = mensagemNaoDoar;
        }
*/
        // com o operador ternário, muda-se para essa:
        // sua definição é (condicao) ? valor_se_verdadeiro : valor_se_falso;

        String resultado = (salario > 5000) ? mensagemDoar : mensagemNaoDoar;

        System.out.println(resultado);


    }
}
