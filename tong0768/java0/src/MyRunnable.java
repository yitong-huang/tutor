package java0.src;

public class MyRunnable implements Runnable {

    @Override
    public void run() {
        System.out.println("hello from runnable");
    }

    public static void main(String[] args) {
        new Thread(new MyRunnable()).start();
    }
}
