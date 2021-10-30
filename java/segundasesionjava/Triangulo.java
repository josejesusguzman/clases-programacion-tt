
/**
 * Write a description of class Triangulo here.
 * 
 * @author (your name) 
 * @version (a version number or a date)
 */
public class Triangulo extends DosDimensiones
{
    String estilo;
    
    //Polimorfismo
    public Triangulo() {
        System.out.println("Primer constructor");
        estilo = "Isoceles";
    }
    
    public Triangulo(String estilo) {
        System.out.println("Segundo constructor");
        this.estilo = estilo;
    }
    
    double area() {
        return (base * altura) / 2;
    }
    
    void showEstilo() {
        System.out.println("El triangulo es: " + estilo);
    }
    
    public static void main() {
        Triangulo triangulo1 = new Triangulo();
        Triangulo triangulo2 = new Triangulo("Isoceles");
        
        hola();
        
        triangulo1.base = 6.0;
        triangulo1.altura = 6.0;
        triangulo1.estilo = "Equilatero";
        
        triangulo2.base = 12.0;
        triangulo2.altura = 20.0;
        
        System.out.println("Triangulo 1");
        triangulo1.showEstilo();
        triangulo1.mostrarDimension();
        System.out.println("El área es igual a: " + triangulo1.area()); 
        
        System.out.println("_________________________");
        
        System.out.println("Triangulo 2");
        triangulo2.showEstilo();
        triangulo2.mostrarDimension();
        System.out.println("El área es igual a: " + triangulo2.area()); 
        
        System.out.println("_________________________");
        
    }
    
    private static void hola() {
        System.out.println("Hola");
    }
}
