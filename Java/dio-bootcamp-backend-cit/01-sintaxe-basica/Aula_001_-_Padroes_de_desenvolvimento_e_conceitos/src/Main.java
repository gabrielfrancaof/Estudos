import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        //meu comentário
        Scanner scanner = new Scanner(System.in);
        System.out.println("Olá, informe o seu nome");
        String name = scanner.next();
        System.out.println("Olá, informe sua idade");
        int age = scanner.nextInt();
        System.out.printf("Olá, %s sua idade é %s \n", name, age);
    }
}