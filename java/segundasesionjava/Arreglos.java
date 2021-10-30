import java.util.*;
/**
 * Write a description of class Arreglos here.
 * 
 * @author (your name) 
 * @version (a version number or a date)
 */
public class Arreglos
{
    public static void main() {
        // Arreglos multidimensionales
        int arreglo[][] = {{1,2,3}, {4,5,6}, {7,8,9}};
        
        for (int i = 0; i < 3; i++) {
            for (int j = 0; j < 3; j++) {
                System.out.print(arreglo[i][j] + " ");
            }
            System.out.println();
        }
    }
    
}
