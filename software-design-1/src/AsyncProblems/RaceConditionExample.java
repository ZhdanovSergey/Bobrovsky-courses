package AsyncProblems;

// Итоговое значение счетчика может быть не правильным, потому что параллельные потоки могут время от времени пытаться обновить его одновременно,
// т.е. 2 потока одновременно получат одинаковое значение счетчика (например 10), каждый поток увеличит полученное значение на 1 (11 в обоих потоках),
// и перезапишет значение счетчика этим значением. В итоге счетчик увеличится не на 2, а только на 1.

// Исправленная реализация
public class RaceConditionExample {

    private static int counter = 0;

    public static int main() {
        
        final Object lock = new Object();
        int numberOfThreads = 10;
        Thread[] threads = new Thread[numberOfThreads];

        for (int i = 0; i < numberOfThreads; i++) {
            threads[i] = new Thread(() -> {
                for (int j = 0; j < 100000; j++) {
                    synchronized (lock) {
                        counter++;
                    }
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

        return counter;
    }
}
