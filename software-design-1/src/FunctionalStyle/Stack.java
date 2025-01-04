package FunctionalStyle;

import java.util.ArrayList;

public final class Stack<T> {
    private final ArrayList<T> elements;

    public Stack() {
        elements = new ArrayList<T>();
    }

    public Stack(ArrayList<T> initialElements) {
        elements = initialElements;
    }

    public Stack<T> push(T data) {
        ArrayList<T> newElements = new ArrayList<T>(elements);
        newElements.add(data);
        return new Stack<T>(newElements);
    }

    public Stack<T> pop() {
        if (isEmpty()) {
            throw new RuntimeException("Стек пуст");
        }

        ArrayList<T> newElements = new ArrayList<T>(elements);
        newElements.remove(newElements.size() - 1);
        return new Stack<T>(newElements);
    }

    public T peek() {
        if (isEmpty()) {
            throw new RuntimeException("Стек пуст");
        }

        return elements.get(elements.size() - 1);
    }

    public boolean isEmpty() {
        return elements.isEmpty();
    }

    public int size() {
        return elements.size();
    }
}