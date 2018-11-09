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
public class EmpleadoFijo extends Empleado {

    double sueldo_fijo, descuento;

    public EmpleadoFijo(String nombre, String apellido, String cedula, double comision_fija, double sueldo_fijo, double descuento) {
        super(nombre, apellido, cedula, comision_fija);
        setDescuento(descuento);
        setSueldo_fijo(sueldo_fijo);
    }

    public double getSueldo_fijo() {
        return sueldo_fijo;
    }

    public void setSueldo_fijo(double sueldo_fijo) {
        this.sueldo_fijo = sueldo_fijo;
    }

    public double getDescuento() {
        return descuento;
    }

    public void setDescuento(double descuento) {
        this.descuento = descuento;
    }

    public double calular_valor_sueldo_final() {
        double sueldo_final = sueldo_fijo - ((sueldo_fijo * descuento) / 100);
        return sueldo_final+comision_fija;
    }

    @Override
    public String toString() {
        return String.format("%s\n\tSueldo Fijo:%s\n\tDescuento del seguro:%s\n\tSueldo Final:%s", super.toString(), getSueldo_fijo(), getDescuento(), calular_valor_sueldo_final());
    }
}
