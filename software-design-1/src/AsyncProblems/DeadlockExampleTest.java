package AsyncProblems;

import static org.junit.Assert.assertEquals;

import org.junit.Test;

public class DeadlockExampleTest {
    @Test
    public void testFixedDeadlockExample() {
        boolean result = DeadlockExample.main();
        assertEquals(true, result);
    }
}
