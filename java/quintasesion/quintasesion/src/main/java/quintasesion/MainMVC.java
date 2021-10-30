/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Main.java to edit this template
 */
package quintasesion;

/**
 *
 * @author jose1
 */
public class MainMVC {

    /**
     * @param args the command line arguments
     */
    public static void main(String[] args) {
        // Ejecución del código
        
        // Obtener los datos de los cursos
        Cursos model = obtenerInfo();
        CursosView view = new CursosView();
        CursosController controller = new CursosController(model, view);
        
        controller.updateView();
        
        controller.setNombreCurso("Python");
        System.out.println("Actualizando cursos");
        controller.updateView();
        
    }
    
    private static Cursos obtenerInfo() {
        Cursos curso = new Cursos();
        curso.setNombreCurso("Java");
        curso.setID(1);
        curso.setCategoriaCurso("Programación");
        return curso;
    }    
}
