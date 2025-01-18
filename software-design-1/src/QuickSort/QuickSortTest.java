package QuickSort;

import static org.junit.Assert.assertTrue;

import java.util.Arrays;

import org.junit.Test;

public class QuickSortTest {
    @Test
    public void testQuickSort() {
        int[] array = {5,4,3,2,1};
        QuickSort.quickSort(array, 0, array.length - 1);
        assertTrue(Arrays.equals(array, new int[] {1,2,3,4,5}));
    }
}
