package OldBugs;

// Этот код правильно компилируется и выполняется без ошибок, но в нём присутствуют следующие логические ошибки:

// - В методе deposit нет проверки на отрицательные суммы, что позволяет увеличить баланс путем депозита отрицательного значения.
// - В методе withdraw нет проверки на отрицательные суммы, что позволяет уменьшить баланс путем попытки снятия отрицательного значения.
// - В методе withdraw нет проверки на достаточность средств на счете, что позволяет уйти в отрицательный баланс банковского счета.

class BankAccount {
    private double balance;

    public BankAccount(double initialBalance) {
        this.balance = initialBalance;
    }

    public void deposit(double amount) {
        balance += amount; // Нет проверки на отрицательную сумму
    }

    public void withdraw(double amount) {
        balance -= amount; // Нет проверки на отрицательную сумму и сверхбаланс
    }

    public double getBalance() {
        return balance;
    }
}

class Main {
    public static void main(String[] args) {
        BankAccount account = new BankAccount(1000);
        System.out.println("Начальный баланс: " + account.getBalance());
        
        account.deposit(500);
        System.out.println("Баланс после депозита 500: " + account.getBalance());
        
        account.withdraw(200);
        System.out.println("Баланс после снятия 200: " + account.getBalance());
        
        account.withdraw(2000);
        System.out.println("Баланс после снятия 2000: " + account.getBalance());
        
        account.deposit(-100); // Некорректный депозит
        System.out.println("Баланс после некорректного депозита -100: " 
          + account.getBalance());
        
        account.withdraw(-50); // Некорректное снятие
        System.out.println("Баланс после некорректного снятия -50: " 
          + account.getBalance());
    }
}