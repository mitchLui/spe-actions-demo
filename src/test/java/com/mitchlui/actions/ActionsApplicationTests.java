package com.mitchlui.actions;

import static org.junit.jupiter.api.Assertions.assertEquals;

import org.junit.jupiter.api.Test;
import org.springframework.boot.test.context.SpringBootTest;

@SpringBootTest
class ActionsApplicationTests {

	@Test
	void contextLoads() {
	}

  @Test
  void testProcessRoot() {
    assertEquals("Hello SPE!", Controller.index());
  }

  @Test 
  void testProcessAddRequest() {
    assertEquals(5, Controller.processAddRequest(2, 3));
  }

  @Test
  void testProcessSubtractRequest() {
    assertEquals(5, Controller.processSubtractRequest(10, 5));
  }

}
