package Threads;

public class ThreadExample {
    private static int counter = 0;

    public static int main() {
        Runnable task = () -> {
            for (int i = 0; i < 1000; i++) {
                incrementCounter();
            }
        };

        Thread thread1 = new Thread(task);
        Thread thread2 = new Thread(task);

        thread1.start();
        thread2.start();

        try {
            thread1.join();
            thread2.join();
        } catch (InterruptedException e) {
            e.printStackTrace();
        }

        return counter;
    }

    
    private static synchronized void incrementCounter() {
        counter++;
    };
}