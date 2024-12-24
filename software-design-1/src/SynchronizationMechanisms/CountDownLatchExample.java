package SynchronizationMechanisms;

import java.util.concurrent.CountDownLatch;

// Использование CountDownLatch для ожидания завершения подготовки всеми участниками команды.

class TeamMember implements Runnable {
    private final CountDownLatch latch;
    private final String name;

    public TeamMember(CountDownLatch latch, String name) {
        this.latch = latch;
        this.name = name;
    }

    @Override
    public void run() {
        try {
            // Имитируем подготовку
            Thread.sleep((long) (Math.random() * 3000));
            System.out.println(name + " has completed preparation.");
        } catch (InterruptedException e) {
            Thread.currentThread().interrupt();
        } finally {
            latch.countDown(); // Уменьшаем счетчик
        }
    }
}

public class CountDownLatchExample {
    public static void main(String[] args) throws InterruptedException {
        int numberOfMembers = 5;
        CountDownLatch latch = new CountDownLatch(numberOfMembers);

        for (int i = 1; i <= numberOfMembers; i++) {
            new Thread(new TeamMember(latch, "Team Member " + i)).start();
        }

        latch.await(); // Ожидаем завершения всех подготовок
        System.out.println("All team members are ready. The race has started!");
    }
}