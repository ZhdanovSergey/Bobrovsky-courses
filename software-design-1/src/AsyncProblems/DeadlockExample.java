package AsyncProblems;

// Каждый из потоков блокирует свой объект, и не разблокирует его до тех пор, пока другой поток не разблокирует свой объект,
// в итоге оба потока ждут завершения друг друга и программа зависает.

// Исправленная реализация
public class DeadlockExample {

    private static final Object lock1 = new Object();
    private static final Object lock2 = new Object();

    public static boolean main() {
        Thread thread1 = new Thread(() -> {
            synchronized (lock1) {
                System.out.println("Thread 1 acquired lock1");

                try { Thread.sleep(50); } 
                catch (InterruptedException e) { e.printStackTrace(); }
            }

            synchronized (lock2) {
                System.out.println("Thread 1 acquired lock2");
            }
        });

        Thread thread2 = new Thread(() -> {
            synchronized (lock2) {
                System.out.println("Thread 2 acquired lock2");

                try { Thread.sleep(50); } 
                catch (InterruptedException e) { e.printStackTrace(); }
            }

            synchronized (lock1) {
                System.out.println("Thread 2 acquired lock1");
            }
        });

        thread1.start();
        thread2.start();

        try {
            thread1.join();
            thread2.join();
        } catch (InterruptedException e) {
            e.printStackTrace();
        }

        return true;
    }
}
