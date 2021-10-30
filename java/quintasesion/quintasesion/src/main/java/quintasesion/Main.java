/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Main.java to edit this template
 */
package quintasesion;

import java.awt.*;
import java.awt.event.*;
import javax.swing.*;

/**
 *
 * @author jose1
 */
public class Main extends JFrame implements ActionListener {

   JButton b1;
   
   Main() {
       this.setLayout(null);
       b1 = new JButton("Buton 1");
       
       b1.setBounds(130, 5, 100, 60);
       
       this.add(b1);
       
       b1.addActionListener(this);
   }
   
   public void actionPerformed(ActionEvent event) {
       if (event.getSource() == b1) {
           System.out.println("Me has presionado papí");
           JOptionPane.showMessageDialog(
                   this,
                   "Aquí me has presionado",
                   "HOLAAAA",
                   JOptionPane.ERROR_MESSAGE
           );
       }
   }
    
    public static void main(String[] args) {
        Main demo = new Main();
        demo.setBounds(200, 200, 400, 300);
        demo.setVisible(true);
    }
}
