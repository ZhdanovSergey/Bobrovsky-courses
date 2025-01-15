package InvariantCycle;

public class InvariantCycle {
    // Инвариант:
    // i: 0 <= i < arr.length
    // res = max(arr[0:i])
    public static int findMax(int[] arr) {
        int res = arr[0];

        // перед началом цикла
        // i = 0, следовательно 0 <= i < arr.length
        // res = arr[i], i = 0 следовательно res = max(arr[0:i])

        for (int i = 0; i < arr.length ; i++)  {
            // после каждой итерации
            // i = i + 1, продолжаем только если i < arr.length, следовательно 0 <= i < arr.length
            // res = max(res, arr[i]) = max(max(arr[0:i-1]),arr[i]) = max(arr[0:i])
            res = Math.max(res, arr[i]);
        }

        return res;
    }
}