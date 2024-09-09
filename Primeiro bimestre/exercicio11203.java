//Um funcionário de uma empresa recebe aumento salarial anualmente. Sabe-se que:
//a) esse funcionário foi contratado em 2005, com salário inicial de R$ 1.000,00;
//b) em 2006 recebeu aumento de 1,5% sobre o salário inicial;
//c) a partir de 2007 (inclusive), os aumentos salariais sempre corresponderam ao dobro do percentual do ano anterior.
//Faça um programa que determine o salário atual desse funcionário.
public class exercicio11203 {
    public static void main(String[] args) {
        double salario = 1000;
        int ano = 2005;
        double percentualDeAumento = 0.015;
        for (int year = ano + 1; year <= 2024; year++) {
            salario = salario + salario * percentualDeAumento;
            percentualDeAumento = percentualDeAumento * 2;
        }
        System.out.println("Seu salário atual é de R$:" + salario);
    }
}
