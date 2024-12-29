package Threads;

import static org.junit.Assert.assertEquals;

import org.junit.Test;

public class ThreadExampleTest {
    @Test
    public void testFixedRaceCondition() {
        int result = ThreadExample.main();
        assertEquals(2000, result);
    }
}
