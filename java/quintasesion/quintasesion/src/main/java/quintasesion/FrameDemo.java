/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package quintasesion;

import java.awt.*;
import java.awt.event.*;
import javax.swing.*;

/**
 *
 * @author jose1
 */
public class FrameDemo {
    
    private static void creacionUI() {
        JFrame frame = new JFrame("Demo");
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        
        JLabel label = new JLabel("Hola mundo");
        label.setPreferredSize(new Dimension(175, 200));
        frame.getContentPane().add(label, BorderLayout.CENTER);
        
        frame.pack();
        frame.setVisible(true);
    }
    
    public static void main(String[] args) {
       javax.swing.SwingUtilities.invokeLater(new Runnable() {
           public void run() {
               creacionUI();
           }
       });
    }
    
}
