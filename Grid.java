import java.awt.*;
import javax.swing.*;
public class Grid extends JPanel {

	public void paint(Graphics g) {
		fetchData clues = new fetchData();
		for (int i = 0; i < 5; i++) {
			g.drawRect(40, (40 + (i * 60)), 60, 60);
			for (int k = 0; k < 5; k++) {
				g.drawRect((40 + (k * 60)), (40 + (i * 60)), 60, 60);
				g.setColor(Color.black);

				if(Character.isDigit(clues.readText().get((i*5)+k+10).charAt(clues.readText().get((i*5)+k+10).length()-1))){
			    	g.drawString(Character.toString(clues.readText().get((i*5)+k+10).charAt(clues.readText().get((i*5)+k+10).length()-1)),(40 + (k * 60))+5, (40 + (i * 60))+15 );
			    	g.drawString(Character.toString(clues.readText().get((i*5)+k+10).charAt(clues.readText().get((i*5)+k+10).length()-3)),(40 + (k * 60))+20, (40 + (i * 60))+35 );
			    }
				else {
					g.drawString(Character.toString(clues.readText().get((i*5)+k+10).charAt(clues.readText().get((i*5)+k+10).length()-1)),(40 + (k * 60))+20, (40 + (i * 60))+35 );
					if(clues.readText().get((i*5)+k+10).charAt(clues.readText().get((i*5)+k+10).length()-1)=='k') {
					    g.fillRect((40 + (k * 60)), (40 + (i * 60)), 60, 60);

						}
				}
				}

			}

		g.drawString("ACROSS", 520, 60);

		for (int i = 0; i < 5; i++) {
			g.drawString(clues.readText().get(i), 520, (80+(i*20)));
		}

		g.drawString("DOWN", 520, 220);
		for (int i = 5; i < 10; i++) {
			g.drawString(clues.readText().get(i), 520, (240+((i-5)*20)));
		}

		g.drawString(clues.date1, 200, 370);
		g.drawString("METONYM", 280, 370);

	}

	public static void main(String[] args) {
		JFrame frame = new JFrame("Mini Puzzle");

		frame.add(new Grid());
		frame.setSize(1300, 550);
		frame.setVisible(true);
		frame.setBackground(Color.white);
		frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
		frame.setResizable(false);
    }


}
