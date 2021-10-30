
/**
 * Write a description of class MiHilo here.
 * 
 * @author (your name) 
 * @version (a version number or a date)
 */
public class MiHilo implements Runnable
{
    Thread hilo;
    static SumArray sumArray = new SumArray();
    int a[];
    int resp;
    
    MiHilo(String nombre, int nums[]) {
        hilo = new Thread(this, nombre);
        a = nums;
    }
    
    public static MiHilo crearHilo(String nombre, int nums[]) {
        MiHilo miHilo = new MiHilo(nombre, nums);
        miHilo.hilo.start();
        return miHilo;
        
    }
    
    public void run() {
        int suma;
        System.out.println(hilo.getName() + " iniciando");
        
        resp = sumArray.sumArray(a);
        System.out.println("Suma para " + hilo.getName() + " es " + resp);
        System.out.println(hilo.getName() + " terminado.");
    }
}
