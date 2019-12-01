import java.util.*;
import java.io.*;
import org.python.util.PythonInterpreter;

public class JythonHelloWorld {
  public static void main(String[] args) throws FileNotFoundException{
    try(PythonInterpreter pyInterp = new PythonInterpreter()) {
      Scanner program=new Scanner(new File("python/HelloWorld.py"));
      String programStr="";
      while (program.hasNextLine()){
          programStr+=program.nextLine()+"\n";
        }
      pyInterp.exec(programStr);
    }
  }
}
