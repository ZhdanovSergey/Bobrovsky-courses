package BoundaryConditionTesting;

import java.util.List;

public class GradeCalculator {
    public static float calculateAverage(List<Integer> grades) {
        if (grades == null || grades.size() == 0) {
            throw new IllegalArgumentException("List must not be null or empty");
        }

        float sum = 0;

        for (int grade : grades) {
            sum += grade;
        }

        return sum / grades.size();
    }
}
