package ComplexCode;

import java.util.Random;
import java.util.Arrays;

public class MultiThreadProcessing {
    private static final int[] data = new int[1_000_000];

    public static int main() {
        Random random = new Random();

        for (int i = 0; i < data.length; i++) {
            data[i] = random.nextInt(100);
        }

        return Arrays.stream(data).parallel().sum();
    }
}