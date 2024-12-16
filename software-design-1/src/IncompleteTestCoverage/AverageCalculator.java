package IncompleteTestCoverage;

public class AverageCalculator {
    public static float calculateAverage(int[] numbers) {
        float sum = 0;

        for (int i : numbers) {
            sum += i;
        }

        return sum / numbers.length;
    }
}
