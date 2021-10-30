
/**
 * Write a description of class SumArray here.
 * 
 * @author (your name) 
 * @version (a version number or a date)
 */
public class SumArray
{
    private int suma;
    
    synchronized int sumArray(int nums[]) {
        suma = 0;
        for (int i = 0; i < nums.length ; i++) {
            suma += nums[i];
            System.out.println("Total acumulado de: " + Thread.currentThread().getName() + " es " + suma);
            
            try {
                Thread.sleep(1000);
            } catch (InterruptedException e) {
                System.out.println("Hilo interrumpido");
            }
        }
        return suma;
    }
    
}
