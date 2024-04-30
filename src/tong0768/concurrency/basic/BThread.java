package tong0768.concurrency.basic;

public class BThread implements Runnable {
    @Override
    public void run() {
        int i = 0;
        while (true) {
            System.out.println("Bthread: " + i++);
        }
    }
}
