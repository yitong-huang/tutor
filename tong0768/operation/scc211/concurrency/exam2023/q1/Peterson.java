package operation.scc211.concurrency.exam2023.q1;

public class Peterson implements Runnable {

    static int tiebreak = 0;
    static boolean[] interested = {false, false};

    private final int id;

    public Peterson(int id) {
        this.id = id;
    }

    @Override
    public void run() {
        getLock();
        System.out.println("thread" + id + ": working");
        releaseLock();
    }

    void getLock() {
        int self = this.id;
        int other = 1 - self;
        interested[self] = true;
        tiebreak = other;
        while (interested[other] && tiebreak == other) {
            // do nothing, just wait
            System.out.println("thread" + id + ": waiting");
        }
    }

    void releaseLock() {
        interested[this.id] = false;
    }

    public static void main(String[] args) {
        new Thread(new Peterson(0)).start();
        new Thread(new Peterson(1)).start();
    }

}
