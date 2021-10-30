
/**
 * Write a description of class SeriesDemo here.
 * 
 * @author (your name) 
 * @version (a version number or a date)
 */
public class SeriesDemo
{
    public static void main() {
        DeTresEnTres serie = new DeTresEnTres();
        serie.setIncremental(3);
        
        DeTresEnTres serie2 = new DeTresEnTres(5);
        serie2.setValorInicial(10);
        
        calcularSerie(serie, serie2);
    }
    
    public static void calcularSerie(DeTresEnTres serie, DeTresEnTres serie2) {
        for (int i = 0; i < 10; i++) {
            System.out.println("Serie de 3 - Siguiente valor es: "  + serie.getSiguiente());
            System.out.println("Serie de 5 - Siguiente valor es: "  + serie2.getSiguiente());
        }
            
    }
}
