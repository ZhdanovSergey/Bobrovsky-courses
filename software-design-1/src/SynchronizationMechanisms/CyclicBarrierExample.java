package SynchronizationMechanisms;

import java.util.concurrent.CyclicBarrier;

// Использование CyclicBarrier для синхронизации участников проекта перед началом следующего этапа.

class ProjectMember implements Runnable {
    private final CyclicBarrier barrier;
    private final String name;

    public ProjectMember(CyclicBarrier barrier, String name) {
        this.barrier = barrier;
        this.name = name;
    }

    @Override
    public void run() {
        try {
            // Имитируем выполнение задачи
            System.out.println(name + " is working on the task...");
            Thread.sleep((long) (Math.random() * 3000));
            System.out.println(name + " has completed the task.");

            // Ожидаем других участников
            barrier.await();
            System.out.println(name + " is ready for the next phase.");
        } catch (Exception e) {
            e.printStackTrace();
        }
    }
}

public class CyclicBarrierExample {
    public static void main(String[] args) {
        int numberOfMembers = 3;
        CyclicBarrier barrier = new CyclicBarrier(numberOfMembers, () -> {
            System.out.println("All team members are ready for the next phase of the project!");
        });

        for (int i = 1; i <= numberOfMembers; i++) {
            new Thread(new ProjectMember(barrier, "Project Member " + i)).start();
        }
    }
}