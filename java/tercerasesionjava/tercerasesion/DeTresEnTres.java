
/**
 * Write a description of class DeTresEnTres here.
 * 
 * @author (your name) 
 * @version (a version number or a date)
 */
public class DeTresEnTres implements SerieNumeros
{    
    int inicial;
    int valor;
    int incremental;
    
    DeTresEnTres() {
        inicial = 0;
        valor = 0;
        incremental = 1;
    }
    
    DeTresEnTres(int incremental) {
        inicial = 0;
        valor = 0;
        this.incremental = incremental;
    }
    
    public void setIncremental(int x) {
        this.incremental = x;
    }
    
    public int getSiguiente() {
        valor += this.incremental;
        return valor;
    }
    
    public void reiniciarSerie() {
        valor = inicial;
    }
    
    public void setValorInicial(int x) {
        inicial = x;
        valor = x;
    }
}
