package exerlista;

import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;

/**
 *
 * @author adalberto
 */
public class ExerLista {

    /**
     * @param args the command line arguments
     */
    public static void main(String[] args) {
        // TODO code application logic here
        Scanner sc = new Scanner(System.in);
        int aux, numero;
        List<Integer> lista = new ArrayList<Integer>();
        while (true) {
            System.out.print("Entre um número diferente de ' 0 ' => ");
            aux = sc.nextInt();
            if (aux != 0) {
                lista.add(aux);
            } else {
                System.out.print("Entre o número para verificar => ");
                aux = sc.nextInt();
                break;
            }
        }

        for (int i = 0; i < lista.size(); i++) {
            for (int j = i + 1; j < lista.size(); j++) {
                if ((lista.get(i) * lista.get(j)) == aux) {
                    System.out.println("Resultado: " + lista.get(i) + " e " + lista.get(j));
                } else {
                    System.out.println("Resultado: não existem tais números");
                }

            }

        }

    }
}
