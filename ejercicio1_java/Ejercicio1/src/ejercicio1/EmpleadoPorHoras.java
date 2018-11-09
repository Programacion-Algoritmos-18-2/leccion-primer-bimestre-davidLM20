/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package ejercicio1;

/**
 *
 * @author David Lopez
 */
public class EmpleadoPorHoras extends Empleado {
    double numero_horas, valor_horas;

    public EmpleadoPorHoras(String nombre, String apellido, String cedula, double comision_fija, double numero_horas, double valor_horas) {
        super(nombre, apellido, cedula, comision_fija);
        setNumero_horas(numero_horas);
        setValor_horas(valor_horas);
        
    }

    public double getNumero_horas() {
        return numero_horas;
    }

    public void setNumero_horas(double numero_horas) {
        this.numero_horas = numero_horas;
    }

    public double getValor_horas() {
        return valor_horas;
    }

    public void setValor_horas(double valor_horas) {
        this.valor_horas = valor_horas;
    }
    
    public double calular_valor_sueldo_final() {
        double sueldo_final = numero_horas * valor_horas;
        return sueldo_final;
    }
   
    @Override
    public String toString() {
        return String.format("%s\n\tNumero horas: %s\n\tValor hora:%s\n\tSueldo Final:%s", super.toString(),getNumero_horas(),getValor_horas(),calular_valor_sueldo_final());
    }
    
    
}
