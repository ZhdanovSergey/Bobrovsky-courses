package QuickSort;

public class QuickSort {
    // P:
    // 0 <= low <= arr.length - 1
    // 0 <= high <= arr.length - 1
    // low < high
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
        //  fact low <= pivot <= high
        //  fact arr[low:pivot] sorted
        //  fact arr[pivot:high] sorted
        //  therefore arr sorted
    }

    // P:
    // 0 <= low <= arr.length - 1
    // 0 <= high <= arr.length - 1
    // low < high
    // Q:
    // low <= result <= high
    // arr[result] == max(arr[low:result])
    // arr[result] == min(arr[result:high])
    private static int partition(int[] arr, int low, int high) {
        int i = low;
        // i == low
        // j == low

        // loop invariant:
        // low <= i <= high
        // low <= j <= high
        // i <= j
        // max(arr[low:i-1]) < arr[high]
        // min(arr[i:j-1]) >= arr[high]

        // fact i == low
        // therefore low <= i <= high

        // fact j == low
        // therefore low <= j <= high

        // fact i == low
        // fact j == low
        // therefore i <= j

        // arr[low:low-1].length == 0
        // fact i == low
        // therefore arr[low:i-1].length == 0
        // every element in an empty set less than arr[high]
        // therefore max(arr[low:i-1]) < arr[high]

        // fact arr[low:low-1].length == 0
        // fact i == low
        // fact j == low
        // therefore arr[i:j-1].length == 0
        // every element in an empty set more than arr[high]
        // therefore min(arr[i:j-1]) >= arr[high]

        // fact low <= i <= high
        // fact low <= j <= high
        // fact i <= j
        // fact max(arr[low:i-1]) < arr[high]
        // fact min(arr[i:j-1]) >= arr[high]
        // therefore initial loop invariant is proven
        for (int j = low; j < high; j++) {
            // fact low <= i <= high
            // fact low <= j-1 <= high
            // fact i <= j-1
            // fact max(arr[low:i-1]) < arr[high]
            // fact min(arr[i:j-2]) >= arr[high]

            // prove that
            // low <= i <= high
            // low <= j <= high
            // i <= j
            // max(arr[low:i-1]) < arr[high]
            // min(arr[i:j-1]) >= arr[high]

            if (arr[j] < arr[high]) {
                int temp = arr[i];
                arr[i] = arr[j];
                arr[j] = temp;
                i++;
            } else {
            }
        }
        // j == high
        
        int temp = arr[i];
        arr[i] = arr[high];
        arr[high] = temp;
        // fact max(arr[low:i-1]) < arr[high]
        // swap arr[high] and arr[i]
        // therefore max(arr[low:i-1]) < arr[i]
        // therefore arr[i] == max(arr[low:i])

        // fact min(arr[i:j-1]) >= arr[high]
        // fact j == high
        // therefore min(arr[i:high-1]) >= arr[high]
        // swap arr[high] and arr[i]
        // therefore min(arr[high], ...arr[i+1:high-1]) >= arr[i]
        // therefore arr[i] == min(arr[i:high])

        // result == i
        // fact low <= i <= high
        // fact arr[i] == max(arr[low:i])
        // fact arr[i] == min(arr[i:high])
        // therefore low <= result <= high
        // therefore arr[result] == max(arr[low:result])
        // therefore arr[result] == min(arr[result:high])
        return i;
    }
}