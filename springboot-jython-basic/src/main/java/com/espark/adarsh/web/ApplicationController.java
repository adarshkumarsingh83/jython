package com.espark.adarsh.web;

import org.python.core.PyInteger;
import org.python.core.PyObject;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.RestController;

@RestController
public class ApplicationController {

    @Autowired
    PyObject sumFunction;

    @GetMapping("/api/sum/{val1}/{val2}")
    public Integer getSum(@PathVariable("val1") Integer val1, @PathVariable("val2") Integer val2) {
        PyObject sum = sumFunction.__call__(new PyInteger(val1), new PyInteger(val2));
        return sum.asInt();
    }
}
