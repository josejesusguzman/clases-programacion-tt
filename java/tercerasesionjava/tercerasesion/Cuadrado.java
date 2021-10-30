
/**
 * Write a description of class Cuadrado here.
 * 
 * @author (your name) 
 * @version (a version number or a date)
 */
public class Cuadrado extends Figura
{
    private double lado;
    
    public Cuadrado(String color, double lado) {
        super(color);
        this.lado = lado;
    }
    
    public double calcularArea() {
        return lado * lado;
    }
}
