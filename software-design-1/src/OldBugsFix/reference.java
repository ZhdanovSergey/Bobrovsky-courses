package OldBugsFix;

// Вывод в консоль сделан исключительно для наглядности.
// На практике соответствующие методы должны возвращать код успеха или ошибки (выброса исключений лучше всегда избегать: на СильныхИдеях прочитайте материалы 86 и 87, как правильно работать с исключениями).

class BankAccountFixRef {
    private double balance;

    public BankAccountFixRef(double initialBalance) {
        this.balance = initialBalance;
    }

    public void deposit(double amount) {
        if (amount > 0) {
            balance += amount;
        } else {
            System.out.println("Сумма депозита должна быть положительной.");
        }
    }

    public void withdraw(double amount) {
        if (amount > 0) {
            if (balance >= amount) {
                balance -= amount;
            } else {
                System.out.println("Недостаточно средств на счете для снятия.");
            }
        } else {
            System.out.println("Сумма снятия должна быть положительной.");
        }
    }

    public double getBalance() {
        return balance;
    }
}
