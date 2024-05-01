package tong0768.scc211.concurrency.exam2023.q1;

public class Main {

    public static void main(String[] args) throws InterruptedException {
        Thread[] addThreads = new Thread[100];
        Share share = new Share();

        for (int i = 0; i < 100; i++) {
            AddThread addThread = new AddThread(share);
            addThread.start();
            addThreads[i] = addThread;
        }

        for (int i = 0; i < 100; i++) {
            addThreads[i].join();
        }

        System.out.println(share.getNum());

    }

}
