
/**
 * Write a description of class Colores here.
 * 
 * @author (your name) 
 * @version (a version number or a date)
 */

public class Colores
{
    public static void main() {
        Color arr[] = Color.values();
        
        for (Color color : arr) {
            System.out.println(color + " esta en el indice " + color.ordinal());
        }
        
        System.out.println(Color.valueOf("ROJO"));
        
    }
}

enum Color {
    ROJO, VERDE, AZUL
}
