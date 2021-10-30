
/**
 * Write a description of class Enums here.
 * 
 * @author (your name) 
 * @version (a version number or a date)
 */
public class Enums
{
    public static void main(String[] args) {
        Transporte tp;
        tp = Transporte.AVION;
        
        System.out.println(tp);
        
        tp = Transporte.TREN;
        
        System.out.println(tp);
        
        switch(tp) {
            case COCHE:
                System.out.println("Este es un auto");
                break;
            case CAMION:
                System.out.println("Este es un CAMIÓN DE CARGA");
                break;
            case AVION:
                System.out.println("Este es un avión que vuela");
                break;
            case BICI:
                System.out.println("Esta es un bici de montaña");
                break;
            case PIE:
                System.out.println("No te vayas a cansar");
                break;
            case TREN:
                System.out.println("Este es un tren bala");
                break;
            case BARCO:
                System.out.println("Este es un barco en alta mar");
                break;
        }
        
        System.out.println("-----------------------------------------");
    }
}
