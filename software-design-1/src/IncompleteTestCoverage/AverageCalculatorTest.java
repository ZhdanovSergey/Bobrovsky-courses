package IncompleteTestCoverage;

import static org.junit.Assert.assertTrue;
import org.junit.Test;

public class AverageCalculatorTest {
    // calling calculateAverage with an empty array would result in divide by zero exception
    @Test
    public void testCalculateAverage() {
        float result = AverageCalculator.calculateAverage(new int[]{ 1, 2, 3 });
        assertTrue("Average should be calculated correctly", result == 2);
    }
}
