package operation.scc211.concurrency.basic;

@SuppressWarnings("InfiniteLoopStatement")
public class AThread extends Thread {

    @Override
    public void run() {
        int i = 0;
        while (true) {
            System.out.println("Athread: " + i++);
        }
    }
}
