/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package quintasesion;

/**
 *
 * @author jose1
 */
public class Cursos  {
    private String NombreCurso;
    private int IDCurso;
    private String CategoriaCurso;
    
    public int getID() {
        return IDCurso;
    }
    
    public void setID(int id) {
        this.IDCurso = id;
    }
    
    public String getNombreCurso() {
        return NombreCurso;
    }
    
    public void setNombreCurso(String NombreCurso) {
        this.NombreCurso = NombreCurso;
    }
    
    public String getCategoriaCurso() {
        return CategoriaCurso;
    }
    
    public void setCategoriaCurso(String CategoriaCurso) {
        this.CategoriaCurso = CategoriaCurso;
    }
    
}
