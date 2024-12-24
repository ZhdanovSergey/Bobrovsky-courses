package SynchronizationMechanisms;

import java.util.concurrent.locks.ReentrantLock;

// Использование ReentrantLock для реализации потокобезопасного банковского счета

class BankAccount {
    private final ReentrantLock lock = new ReentrantLock();
    private double balance;

    public BankAccount(double initialBalance) {
        this.balance = initialBalance;
    }

    public void deposit(double amount) {
        lock.lock();
        try {
            balance += amount;
            System.out.printf("Deposited: %.2f, New Balance: %.2f%n", amount, balance);
        } finally {
            lock.unlock();
        }
    }

    public void withdraw(double amount) {
        lock.lock();
        try {
            if (balance >= amount) {
                balance -= amount;
                System.out.printf("Withdrew: %.2f, New Balance: %.2f%n", amount, balance);
            } else {
                System.out.printf("Withdrawal of %.2f failed, Insufficient funds: %.2f%n", amount, balance);
            }
        } finally {
            lock.unlock();
        }
    }

    public double getBalance() {
        return balance;
    }
}

public class ReentrantLockExample {
    public static void main(String[] args) throws InterruptedException {
        BankAccount account = new BankAccount(1000);
        Thread t1 = new Thread(() -> {
            account.deposit(200);
            account.withdraw(150);
        });
        Thread t2 = new Thread(() -> {
            account.withdraw(500);
            account.deposit(100);
        });

        t1.start();
        t2.start();
        t1.join();
        t2.join();
        System.out.printf("Final Balance: %.2f%n", account.getBalance());
    }
}