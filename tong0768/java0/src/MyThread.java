package java0.src;

public class MyThread extends Thread {

    @Override
    public void run() {
        System.out.println("hello from thread");
    }

    public static void main(String[] args) {
        new MyThread().start();
    }
}


