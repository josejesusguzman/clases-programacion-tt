/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package quintasesion;

/**
 *
 * @author jose1
 */
public class CursosController {
    private Cursos model;
    private CursosView view;
    
    public CursosController(Cursos model, CursosView view) {
        this.model = model;
        this.view = view;
    }
    
    public void setNombreCurso(String curso) {
        model.setNombreCurso(curso + "1111111");
    }
    
    public String getNombreCurso() {
        return model.getNombreCurso();
    }
    
    public int getID() {
        return model.getID();
    }
    
    public void setID(int id) {
        model.setID(id);
    }
    
    public String getCategoriaCurso() {
        return model.getCategoriaCurso();
    }
    
    public void setCategoriaCurso(String categoriaCurso) {
        model.setCategoriaCurso(categoriaCurso);
    }
    
    public void updateView() {
        view.detallesCurso(
                model.getNombreCurso(),
                model.getCategoriaCurso(),
                model.getID());
    }
    
}
