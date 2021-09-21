import java.util.*;

/**
 * COMENTARIOS
 * Quien hizo este código
 * Que hace
 * Licencia
 * Para que funciona esta clase
 */

/**
 * Modificadores de acceso
 * public - 
 * private
 * protected
 */
// Esta es una clase
public class Persona {
    
    public static final String especie = "humano";
    
    // Colores de piel
    public static final String colorCapuccino = "Capuccino";
    public static final String colorAmarillo = "Amarillo";
    public static final String colorRGB = "RGB";
    public static final String colorRosa = "Rosa";
    public static final String colorGuero = "Güero";
    public static final String colorMoreno = "Moreno";
    public static final String colorChokomilk = "Chokomilk";
    public static final String colorClaro = "Claro";
    public static final String colorCanela = "Canela";
    public static final String colorApiñonado = "Apiñonao";
    public static final String colorNaranja = "Naranja";
    public static final String colorXD = "XD";
    
    //Dato entero - Números enteros: -50, 5 0 1 12000
    private int colorPiel; // 1 - piel morena
    private String nombres; // "Jesus"
    private boolean conVida; // 1 - 0 true - false verdadero - falso
    private char inicial; // S
    private double estaturaMetros; // 1.75
    private Date fechaNacimiento; // 28-09-1995
    
    // Getter y setters
    public void setColorPiel(int colorPiel) {
        this.colorPiel = colorPiel;
    }
    
    public String getColorPiel() {
        /**
         * Estructuras de control
         * IF - IF ELSE - SWITCH - WHILE - DO WHILE - FOR
         */

        switch(this.colorPiel) {
            case 1:
                return colorCapuccino;
            case 2:
                return colorAmarillo;
            case 3:
                return colorRGB;
            case 4:
                return colorRosa;
            case 5:
                return colorGuero;
            case 6:
                return colorMoreno;
            case 7:
                return colorChokomilk;
            case 8:
                return colorClaro;
            case 9:
                return colorCanela;
            case 10:
                return colorApiñonado;
            case 11:
                return colorNaranja;
            default:
                return colorXD;
        }
    }
    
    public double getEstatura() {
        return this.estaturaMetros;
    }
    
    //Constructor
    public Persona() {
        this.colorPiel = 1;
        this.nombres = "Jose Jesus";
        this.conVida = true;
        this.inicial = 'J';
        this.estaturaMetros = 1.75;
        this.fechaNacimiento = new Date();
    }
    
    //Polimorfismo - Hacer varios constructores con diferente comportamiento
    public Persona(String nombre) {
        this.nombres = nombre;
        this.colorPiel = 2;
    }
    
    public static void main(){
        
        boolean seguir = true;
        
        Persona jesus = new Persona();
        System.out.println(Persona.especie);
        System.out.println(jesus.nombres + " es de color de piel " + jesus.getColorPiel());
        System.out.println("----------------------------------------");
        /*Persona marino = new Persona("Marino");
        System.out.println(marino.nombres + " es de color de piel " + marino.getColorPiel());
        System.out.println("----------------------------------------");*/
        
        while (seguir) {
            
            Scanner scanner = new Scanner(System.in);
            System.out.println("Escribe tu nombre");
            String nombrePersona = scanner.next();
            
            Persona persona = new Persona(nombrePersona);
            System.out.println(persona.nombres + " es de color de piel " + persona.getColorPiel());
            
            System.out.println("¿Quieres hacerlo de nuevo? 1) Si 0) No");
            try {
                seguir =  scanner.nextBoolean();
            } catch (Exception e) {
                System.out.println(seguir + " N¿no es la respuesta que buscaba. Intenta de nuevo");
            }
        }
        System.out.println("Adios perro!!!");
        
        // Ciclo i < 2
        for (int i = 0; i <= 2; i++) {
            System.out.println(jesus.nombres + " es mide " + jesus.getEstatura());
        }
        
    }
    
}