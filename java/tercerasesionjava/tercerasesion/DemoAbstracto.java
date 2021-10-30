import java.util.Scanner;
/**
 * Write a description of class DemoAbstracto here.
 * 
 * @author (your name) 
 * @version (a version number or a date)
 */
public class DemoAbstracto
{
    public static void main() {
        String colorCuadrado;
        double ladoCuadrado;
        
        Scanner teclado = new Scanner(System.in);
        
        System.out.println("Introduce el color del cuadrado:");
        colorCuadrado = teclado.nextLine();
        
        System.out.println("Introduce el lado del cuadrado:");
        ladoCuadrado = teclado.nextDouble();
        
        Cuadrado cuadro = new Cuadrado(colorCuadrado, ladoCuadrado);
        System.out.println("El área del cuadrado " + cuadro.getColor() + " es: " + cuadro.calcularArea());
    }
}
