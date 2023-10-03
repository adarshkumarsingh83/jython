# To generate the java file 

```
package com.espark.adarsh;

public class Wish {
   public void welcome() {
      System.out.println("Hello World!");
   }
   public void welcome(String name) {
      System.out.printf("Hello %s!", name);
   }
}
```

# To compile the java file 
* javac -d  . Wish.java

# permission to .class file 
* sudo chmod 777 com/espark/adarsh/Wish.class

# Create a jar file 
* jar -cvf wish.jar ./manifest.mf com/espark/adarsh/Wish.class

# To execute the python code  
* java -jar ../jython-standalone-2.7.2.jar  main.py


