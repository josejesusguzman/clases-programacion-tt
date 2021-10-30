
/**
 * Write a description of class Sincronizacion here.
 * 
 * @author (your name) 
 * @version (a version number or a date)
 */
public class Sincronizacion
{
    public static void main(String[] args) {
        int a[] = { 1, 2, 3, 4, 5, 6 };
        
        MiHilo hilo1 = MiHilo.crearHilo("suma 1", a);
        MiHilo hilo2 = MiHilo.crearHilo("suma 2", a);
        
        try {
            hilo1.hilo.join();
            hilo2.hilo.join();
        } catch(InterruptedException e) {
            System.out.println("Hilo principal interrumpido");
        }
        
    }
}
