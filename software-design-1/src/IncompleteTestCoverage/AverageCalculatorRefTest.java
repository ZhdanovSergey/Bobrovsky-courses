package IncompleteTestCoverage;

import static org.junit.Assert.assertEquals;
import static org.junit.Assert.assertThrows;

import org.junit.Test;

public class AverageCalculatorRefTest {        
    @Test
    public void testCalculateAverageWithPositiveNumbers() {
        AverageCalculator calculator = new AverageCalculator();
        int[] numbers = {1, 2, 3, 4, 5};
        double result = calculator.calculateAverage(numbers);
        assertEquals(3.0, result, 0.001);
    }

    @Test
    public void testCalculateAverageWithNegativeNumbers() {
        AverageCalculator calculator = new AverageCalculator();
        int[] numbers = {-1, -2, -3, -4, -5};
        double result = calculator.calculateAverage(numbers);
        assertEquals(-3.0, result, 0.001);
    }

    @Test
    public void testCalculateAverageWithMixedNumbers() {
        AverageCalculator calculator = new AverageCalculator();
        int[] numbers = {1, -2, 3, -4, 5};
        double result = calculator.calculateAverage(numbers);
        assertEquals(0.6, result, 0.001);
    }

    // Дополнительные тесты, которые не были написаны:
    @Test
    public void testCalculateAverageWithEmptyArray() {
        AverageCalculator calculator = new AverageCalculator();
        int[] numbers = {};
        assertThrows(IllegalArgumentException.class, () -> {
            calculator.calculateAverage(numbers);
        });
    }

    @Test
    public void testCalculateAverageWithNullArray() {
        AverageCalculator calculator = new AverageCalculator();
        int[] numbers = null;
        assertThrows(IllegalArgumentException.class, () -> {
            calculator.calculateAverage(numbers);
        });
    }
}
