package operation.scc211.concurrency.basic;

@SuppressWarnings({"InfiniteLoopStatement", "unused"})
public class BThread implements Runnable {
    @Override
    public void run() {
        int i = 0;
        while (true) {
            System.out.println("Bthread: " + i++);
        }
    }
}
