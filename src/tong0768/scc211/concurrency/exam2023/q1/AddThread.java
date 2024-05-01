package tong0768.scc211.concurrency.exam2023.q1;

public class AddThread extends Thread {

    private final Share share;

    public AddThread(Share share) {
        this.share = share;
    }

    @Override
    public void run() {
        share.add();
    }
}
