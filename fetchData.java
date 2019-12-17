import java.time.LocalDate;
import java.util.ArrayList;
import java.io.*;
import java.nio.file.Path;
import java.nio.file.Paths;

public class fetchData {
    LocalDate date = LocalDate.now(); // Create a date object
    String date1 = " "+ date.getDayOfMonth()+"."+ date.getMonthValue()+"."+date.getYear();
    File fileName = new File("C:\\Users\\hp pc\\Desktop\\"+"Puzzle-"+date.getMonthValue()+"-"+date.getDayOfMonth()+".txt");
    String line = null ;
    
    public fetchData() {}
    
    public ArrayList<String> readText() {
        ArrayList<String> acrossClues = new ArrayList<String>();
        ArrayList<String> downClues = new ArrayList<String>();
        ArrayList<String> blocks = new ArrayList<String>();
    try {
        // FileReader reads text files in the default encoding.
        FileReader fileReader = new FileReader(fileName);

        // Always wrap FileReader in BufferedReader.
        BufferedReader bufferedReader = new BufferedReader(fileReader);

        while((line = bufferedReader.readLine()) != null) {
            if (line.charAt(0)== 'A'){
            	String strOut= line.substring(7, line.length());
            	acrossClues.add(strOut);
            }
            else if (line.charAt(0)== 'D') {
            	String strOut= line.substring(5, line.length());
            	downClues.add(strOut);
            }      
            else {
            	String strOut= line.substring(3, line.length());	
            	blocks.add(strOut);
            }
            }
            
        
        bufferedReader.close();   
        acrossClues.addAll(downClues);
        acrossClues.addAll(blocks);
        return acrossClues;
    }
    catch(FileNotFoundException ex) {
        System.out.println("Unable to open file '" + fileName + "'");   
        return null;
    }
    catch(IOException ex) {
        System.out.println("Error reading file '"+ fileName + "'");          
        return null;
    }
}
    
}
