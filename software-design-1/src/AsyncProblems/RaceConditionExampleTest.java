package AsyncProblems;

import static org.junit.Assert.assertEquals;

import org.junit.Test;

public class RaceConditionExampleTest {
    @Test
    public void testFixedRaceCondition() {
        int result = RaceConditionExample.main();
        assertEquals(100000 * 10, result);
    }
}
