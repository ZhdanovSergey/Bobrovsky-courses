package AsyncProblems;

// Используем механизм синхронизации: метод increment объявлен как synchronized, что гарантирует, что только один поток будет выполнять этот метод в одно время.

public class RaceConditionFixedRef {

    private static int counter = 0;

    public static synchronized void increment() {
        counter++;
    }

    public static void main(String[] args) {
        int numberOfThreads = 10;
        Thread[] threads = new Thread[numberOfThreads];

        for (int i = 0; i < numberOfThreads; i++) {
            threads[i] = new Thread(() -> {
                for (int j = 0; j < 100000; j++) {
                    increment();
                }
            });
            threads[i].start();
        }

        for (int i = 0; i < numberOfThreads; i++) {
            try {
                threads[i].join();
            } catch (InterruptedException e) {
                e.printStackTrace();
            }
        }

        System.out.println("Final counter value: " + counter);
    }
}