package com.espark.adarsh.config;

import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;
import org.python.core.PyObject;
import org.python.util.PythonInterpreter;
@Configuration
public class ApplicationConfig {


    @Bean
    PyObject pyObject(){
        try (PythonInterpreter pyInterp = new PythonInterpreter()) {
            pyInterp.execfile(ClassLoader.getSystemResourceAsStream("scripts/add-script.py"));
            PyObject sumFunction = pyInterp.get("add");
            return sumFunction;
        }
    }
}
