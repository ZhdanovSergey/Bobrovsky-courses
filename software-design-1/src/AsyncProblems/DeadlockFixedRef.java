package AsyncProblems;

// В исходном примере поток thread1 сначала захватывает lock1, а затем пытается захватить lock2, в то время как thread2 сначала захватывает lock2, а затем пытается захватить lock1. Это и создаёт условие deadlock, так как каждый поток блокируется, ожидая освобождения захваченной другим потоком блокировки.
// В исправленном примере и thread1, и thread2 захватывают блокировки в одном и том же порядке: сначала lock1, а затем lock2. Это предотвращает ситуацию, когда один поток ждет захвата замка, удерживаемого другим потоком, и наоборот.

public class DeadlockFixedRef {

    private static final Object lock1 = new Object();
    private static final Object lock2 = new Object();

    public static void main(String[] args) {
        Thread thread1 = new Thread(() -> {
            synchronized (lock1) {
                System.out.println("Thread 1 acquired lock1");

                try { Thread.sleep(50); } catch (InterruptedException e) {}

                synchronized (lock2) {
                    System.out.println("Thread 1 acquired lock2");
                }
            }
        });

        Thread thread2 = new Thread(() -> {
            synchronized (lock1) {
                System.out.println("Thread 2 acquired lock1");

                try { Thread.sleep(50); } catch (InterruptedException e) {}

                synchronized (lock2) {
                    System.out.println("Thread 2 acquired lock2");
                }
            }
        });

        thread1.start();
        thread2.start();
    }
}