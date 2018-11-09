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
public class EmpleadoPorSemana extends Empleado {

    double numero_semana, valor_por_semana;

    public EmpleadoPorSemana(String nombre, String apellido, String cedula, double comision_fija, double numero_horas, double valor_horas) {
        super(nombre, apellido, cedula, comision_fija);
        setNumero_semana(numero_horas);
        setValor_por_semana(valor_horas);

    }

    public double getNumero_semana() {
        return numero_semana;
    }

    public void setNumero_semana(double numero_semana) {
        this.numero_semana = numero_semana;
    }

    public double getValor_por_semana() {
        return valor_por_semana;
    }

    public void setValor_por_semana(double valor_por_semana) {
        this.valor_por_semana = valor_por_semana;
    }

    public double calular_valor_sueldo_final() {
        double sueldo_final = numero_semana * valor_por_semana;
        return sueldo_final;
    }

    @Override
    public String toString() {
        return String.format("%s\n\tNumero de semanas:%s\n\tValor Semanal:%s\n\tSueldo Final:%s\n", super.toString(), getNumero_semana(), getValor_por_semana(), calular_valor_sueldo_final());
    }

}
