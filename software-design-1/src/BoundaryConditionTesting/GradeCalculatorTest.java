package BoundaryConditionTesting;

import java.util.Arrays;

import static org.junit.Assert.assertEquals;
import static org.junit.Assert.assertThrows;
import org.junit.Test;

public class GradeCalculatorTest {
    @Test
    public void testCalculateAverageWithPositiveNumbers() {
        float result = GradeCalculator.calculateAverage(Arrays.asList(1, 2, 3, 4, 5));
        assertEquals(3.0, result, 0.001);
    }

    @Test
    public void testCalculateAverageWithNegativeNumbers() {
        float result = GradeCalculator.calculateAverage(Arrays.asList(-1, -2, -3, -4, -5));
        assertEquals(-3.0, result, 0.001);
    }

    @Test
    public void testCalculateAverageWithMixedNumbers() {
        double result = GradeCalculator.calculateAverage(Arrays.asList(1, -2, 3, -4, 5));
        assertEquals(0.6, result, 0.001);
    }

    @Test
    public void testCalculateAverageWithEmptyArray() {
        assertThrows(IllegalArgumentException.class, () -> {
            GradeCalculator.calculateAverage(Arrays.asList());
        });
    }

    @Test
    public void testCalculateAverageWithNullArray() {
        assertThrows(IllegalArgumentException.class, () -> {
            GradeCalculator.calculateAverage(null);
        });
    }
}
