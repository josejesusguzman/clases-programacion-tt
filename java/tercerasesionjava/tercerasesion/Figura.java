/**
 * Abstract class Figura - write a description of the class here
 * 
 * @author: 
 * Date: 
 */
public abstract class Figura
{
    private String color;
    
    public Figura(String color) {
        this.color = color;
    }
    
    public abstract double calcularArea();
    
    public String getColor() {
        return color;
    }
 }
