package QuickSort;

public class QuickSort {
    // P:
    //     0 <= low <= arr.length - 1
    //     0 <= high <= arr.length - 1
    //     low < high
    // void quickSort(int[] arr, int low, int high)
    // Q: arr sorted
    public static void quickSort(int[] arr, int low, int high) {
        // fact 0 <= low <= arr.length - 1
        // fact 0 <= high <= arr.length - 1
        // fact low < high
        int pivot = partition(arr, low, high);
        // low <= pivot <= high
        // arr[pivot] == max(arr[low:pivot])
        // arr[pivot] == min(arr[pivot:high])
        if (low < pivot - 1) {
            quickSort(arr, low, pivot - 1);
            // arr[low:pivot-1] sorted
            // fact arr[pivot] == max(arr[low:pivot])
            // therefore arr[low:pivot] sorted
        } else {
            // low >= pivot - 1
            // fact low <= pivot <= high
            // therefore pivot == (low or low+1)
            // fact arr[pivot] == max(arr[low:pivot])
            // therefore arr[low:pivot] sorted
        }

        if (pivot + 1 < high) {
            quickSort(arr, pivot + 1, high);
            // arr[pivot+1:high] sorted
            // fact arr[pivot] == min(arr[pivot:high])
            // therefore arr[pivot:high] sorted
        } else {
            // pivot + 1 >= high
            // fact low <= pivot <= high
            // therefore pivot == (high-1 or high)
            // fact arr[pivot] == min(arr[pivot:high])
            // therefore arr[pivot:high] sorted
        }
        //  fact arr[low:pivot] sorted
        //  fact arr[pivot:high] sorted
        //  fact low <= pivot <= high
        //  therefore arr sorted
    }

    // P:
    //     0 <= low <= arr.length - 1
    //     0 <= high <= arr.length - 1
    //     low < high
    // int partition(int[] arr, int low, int high)
    // Q:
    //     low <= result <= high
    //     arr[result] == max(arr[low:result])
    //     arr[result] == min(arr[result:high])
    private static int partition(int[] arr, int low, int high) {
        int i = low;

        // I:  i in range(low, high) and
        // j in range(low, high) and my brain hurts
        for (int j = low; j <= high; j++) {
            if (arr[j] <= arr[high]) {
                int temp = arr[i];
                arr[i] = arr[j];
                arr[j] = temp;
                i++;
            }
        }

        return --i;
    }
}