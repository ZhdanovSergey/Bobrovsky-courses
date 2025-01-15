package HoareTriples;

public class HoareTriplesRef {
    // предусловие: аргументы - целые числа
    // постусловие: результат - наибольший из модулей чисел-аргументов
    public static int maxAbs(int a, int b) {
        int absA = abs(a);
        // absA - модуль числа a
        int absB = abs(b);
        // absB - модуль числа b
        return max(absA, absB);
    }
    
    // предусловие: аргументы - целые числа
    // постусловие: результат - наибольшее число из переданных в аргументы
    private static int max(int a, int b) {
        return a > b ? a : b;
    }
    
    // предусловие: аргумент - целое число
    // постусловие: результат - модуль числа-аргумента
    private static int abs(int a) {
        return a > 0 ? a : -a;
    }
}