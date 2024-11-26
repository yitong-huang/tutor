package operation.scc211.concurrency.basic;

public class AThread extends Thread {

    @Override
    public void run() {
        int i = 0;
        while (true) {
            System.out.println("Athread: " + i++);
        }
    }
}
