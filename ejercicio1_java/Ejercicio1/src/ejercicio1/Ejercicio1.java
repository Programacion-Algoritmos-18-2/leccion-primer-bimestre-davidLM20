/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package ejercicio1;

import java.util.Scanner;

/**
 *
 * @author David Lopez
 */
public class Ejercicio1 {

    /**
     * @param args the command line arguments
     */
    public static void main(String[] args) {
        // TODO code application logic here
        Scanner entrada = new Scanner(System.in);
        Empleado e = new Empleado("Luis", "Benitez", "110001", 0);
        System.out.println(e);

        System.out.println("Ingrese comision");
        double comision = entrada.nextDouble();
        EmpleadoFijo e1 = new EmpleadoFijo("Ana", "Diaz", "110023", comision, 20, 10);
        System.out.println(e1);

        entrada.nextLine();
        System.out.println("Ingrese el nombre");
        String nombre = entrada.nextLine();

        EmpleadoPorHoras e2 = new EmpleadoPorHoras(nombre, "Andrade", "112233", 20, 15, 20.2);
        System.out.println(e2);
        
        EmpleadoPorSemana e3 = new EmpleadoPorSemana("Lucas", "Adams", "1102332", 30, 3, 2305);
        System.out.println(e3);
    }

}
