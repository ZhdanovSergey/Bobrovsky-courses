package IncompleteTestCoverage;

import static org.junit.Assert.assertEquals;
import static org.junit.Assert.assertThrows;

import org.junit.Test;

public class AverageCalculatorRefTest {        
    @Test
    public void testCalculateAverageWithPositiveNumbers() {
        int[] numbers = {1, 2, 3, 4, 5};
        double result = AverageCalculator.calculateAverage(numbers);
        assertEquals(3.0, result, 0.001);
    }

    @Test
    public void testCalculateAverageWithNegativeNumbers() {
        int[] numbers = {-1, -2, -3, -4, -5};
        double result = AverageCalculator.calculateAverage(numbers);
        assertEquals(-3.0, result, 0.001);
    }

    @Test
    public void testCalculateAverageWithMixedNumbers() {
        int[] numbers = {1, -2, 3, -4, 5};
        double result = AverageCalculator.calculateAverage(numbers);
        assertEquals(0.6, result, 0.001);
    }

    // Дополнительные тесты, которые не были написаны:
    @Test
    public void testCalculateAverageWithEmptyArray() {
        int[] numbers = {};
        assertThrows(IllegalArgumentException.class, () -> {
            AverageCalculator.calculateAverage(numbers);
        });
    }

    @Test
    public void testCalculateAverageWithNullArray() {
        int[] numbers = null;
        assertThrows(IllegalArgumentException.class, () -> {
            AverageCalculator.calculateAverage(numbers);
        });
    }
}
