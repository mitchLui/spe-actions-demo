package com.mitchlui.actions;

import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

@RestController
public class Controller {

  @RequestMapping("/")
  public static String index() {
    return "Hello World!";
  }

  @RequestMapping("/add") 
  public static int processAddRequest(int a, int b) {
    return MyMath.add(a, b);
  }


  @RequestMapping("/subtract")
  public static int processSubtractRequest(int a, int b) {
    return MyMath.subtract(a, b);
  }
}
